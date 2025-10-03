from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Notification, Conversation, Message
from .serializers import (
    ProfileSerializer, UserSerializer, NotificationSerializer,
    ConversationSerializer, MessageSerializer, UserRegistrationSerializer
)


class RegisterView(generics.CreateAPIView):
    """User registration endpoint"""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class MyProfileView(generics.RetrieveUpdateAPIView):
    """Get and update current user's profile"""
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user.profile
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ProfileDetailView(generics.RetrieveAPIView):
    """Get any user's profile by username"""
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'
    
    def get_queryset(self):
        return Profile.objects.select_related('user').prefetch_related('following', 'followers')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, username):
    """Toggle follow/unfollow a user"""
    target_user = get_object_or_404(User, username=username)
    
    if target_user == request.user:
        return Response(
            {'error': 'You cannot follow yourself'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    profile = request.user.profile
    target_profile = target_user.profile
    
    if target_profile in profile.following.all():
        profile.following.remove(target_profile)
        # Delete follow notification when unfollowing
        Notification.objects.filter(
            recipient=target_user,
            actor=request.user,
            verb='follow'
        ).delete()
        return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)
    else:
        profile.following.add(target_profile)
        # Create follow notification
        Notification.objects.create(
            recipient=target_user,
            actor=request.user,
            verb='follow'
        )
        return Response({'status': 'followed'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_follower(request, username):
    """Remove a follower from your followers list"""
    follower_user = get_object_or_404(User, username=username)
    
    if follower_user == request.user:
        return Response(
            {'error': 'Invalid operation'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Remove the follower by removing yourself from their following list
    follower_profile = follower_user.profile
    current_profile = request.user.profile
    
    if current_profile in follower_profile.following.all():
        follower_profile.following.remove(current_profile)
        # Delete follow notification
        Notification.objects.filter(
            recipient=request.user,
            actor=follower_user,
            verb='follow'
        ).delete()
        return Response({'status': 'removed'}, status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': 'User is not following you'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([AllowAny])
def get_followers(request, username):
    """Get list of followers for a user"""
    target_user = get_object_or_404(User, username=username)
    target_profile = target_user.profile
    
    # Get all profiles that are following this user
    followers = target_profile.followers.all()
    
    # Get the User objects from these profiles
    follower_users = [follower.user for follower in followers]
    
    # Serialize with is_following field for current user
    serializer = UserSerializer(follower_users, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_following(request, username):
    """Get list of users that this user is following"""
    target_user = get_object_or_404(User, username=username)
    target_profile = target_user.profile
    
    # Get all profiles that this user is following
    following = target_profile.following.all()
    
    # Get the User objects from these profiles
    following_users = [followed.user for followed in following]
    
    # Serialize with is_following field for current user
    serializer = UserSerializer(following_users, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_users(request):
    """Search users by username"""
    query = request.GET.get('q', '')
    if query:
        users = User.objects.filter(username__icontains=query)[:20]
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
    return Response([])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_suggestions(request):
    """Get user suggestions for people you might want to follow"""
    current_user = request.user
    current_profile = current_user.profile
    
    # Get users that the current user is already following
    following_profiles = current_profile.following.all()
    following_user_ids = [profile.user.id for profile in following_profiles]
    
    # Exclude current user and users already followed
    exclude_ids = following_user_ids + [current_user.id]
    
    # Get users followed by people you follow (friends of friends)
    suggested_profiles = Profile.objects.filter(
        followers__in=following_profiles
    ).exclude(user__id__in=exclude_ids).distinct()[:10]
    
    # If not enough suggestions, get random users
    if suggested_profiles.count() < 5:
        additional_users = User.objects.exclude(
            id__in=exclude_ids
        ).order_by('?')[:10]
        
        # Combine both suggestion lists
        all_suggestions = list(suggested_profiles.values_list('user', flat=True)) + list(additional_users.values_list('id', flat=True))
        # Remove duplicates and limit
        unique_ids = list(dict.fromkeys(all_suggestions))[:10]
        users = User.objects.filter(id__in=unique_ids)
    else:
        users = [profile.user for profile in suggested_profiles]
    
    serializer = UserSerializer(users, many=True, context={'request': request})
    return Response(serializer.data)


class NotificationListView(generics.ListAPIView):
    """List all notifications for current user"""
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def mark_notifications_read(request):
    """Mark all notifications as read"""
    Notification.objects.filter(
        recipient=request.user,
        is_read=False
    ).update(is_read=True)
    return Response({'status': 'success'})


class ConversationListView(generics.ListAPIView):
    """List all conversations for current user"""
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)
    
    def get_serializer_context(self):
        return {'request': self.request}


class ConversationDetailView(generics.RetrieveAPIView):
    """Get conversation details"""
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)
    
    def get_serializer_context(self):
        return {'request': self.request}


class MessageListView(generics.ListCreateAPIView):
    """List messages in a conversation and create new messages"""
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        conversation_id = self.kwargs.get('conversation_id')
        return Message.objects.filter(conversation_id=conversation_id)
    
    def list(self, request, *args, **kwargs):
        """Override list to mark messages as read when fetched"""
        response = super().list(request, *args, **kwargs)
        
        # Mark all unread messages in this conversation as read
        conversation_id = self.kwargs.get('conversation_id')
        Message.objects.filter(
            conversation_id=conversation_id,
            is_read=False
        ).exclude(sender=request.user).update(is_read=True)
        
        return response
    
    def perform_create(self, serializer):
        conversation_id = self.kwargs.get('conversation_id')
        conversation = get_object_or_404(Conversation, id=conversation_id)
        
        # Check if user is participant
        if self.request.user not in conversation.participants.all():
            return Response(
                {'error': 'You are not a participant in this conversation'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer.save(
            sender=self.request.user,
            conversation=conversation
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_conversation(request):
    """Create a new conversation with a user"""
    username = request.data.get('username')
    if not username:
        return Response(
            {'error': 'Username is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    other_user = get_object_or_404(User, username=username)
    
    if other_user == request.user:
        return Response(
            {'error': 'You cannot create a conversation with yourself'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Check if conversation already exists
    existing = Conversation.objects.filter(
        participants=request.user
    ).filter(participants=other_user).first()
    
    if existing:
        serializer = ConversationSerializer(existing, context={'request': request})
        return Response(serializer.data)
    
    # Create new conversation
    conversation = Conversation.objects.create()
    conversation.participants.add(request.user, other_user)
    
    serializer = ConversationSerializer(conversation, context={'request': request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset_request(request):
    """Request password reset via email"""
    email = request.data.get('email')
    
    if not email:
        return Response(
            {'error': 'Email is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        user = User.objects.get(email=email)
        
        # Generate password reset token
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        
        # Create reset link
        reset_link = f"{settings.FRONTEND_URL or 'http://localhost:8000'}/reset-password/{uid}/{token}/"
        
        # Send email
        send_mail(
            subject='Password Reset Request',
            message=f'Click the link below to reset your password:\n\n{reset_link}\n\nThis link will expire in 24 hours.',
            from_email=settings.DEFAULT_FROM_EMAIL or 'noreply@instagram-clone.com',
            recipient_list=[email],
            fail_silently=False,
        )
        
        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
    
    except User.DoesNotExist:
        # Don't reveal if email exists for security
        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {'error': 'Failed to send reset email'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset_confirm(request):
    """Confirm password reset with token"""
    uidb64 = request.data.get('uid')
    token = request.data.get('token')
    new_password = request.data.get('new_password')
    
    if not all([uidb64, token, new_password]):
        return Response(
            {'error': 'Missing required fields'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Decode user ID
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        
        # Verify token
        if not default_token_generator.check_token(user, token):
            return Response(
                {'error': 'Invalid or expired token'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Set new password
        user.set_password(new_password)
        user.save()
        
        return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
    
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return Response(
            {'error': 'Invalid reset link'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_jwt_token(request):
    """Get JWT token for currently authenticated user (for OAuth users)"""
    from rest_framework_simplejwt.tokens import RefreshToken

    refresh = RefreshToken.for_user(request.user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
