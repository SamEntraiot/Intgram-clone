from rest_framework import serializers
from .models import Post, Comment, Story, StoryView
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_avatar = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'author_username', 'author_avatar', 
                  'text', 'created_at')
        read_only_fields = ('post', 'author', 'created_at')
    
    def get_author_avatar(self, obj):
        """Safely get author avatar URL"""
        try:
            if hasattr(obj.author, 'profile') and obj.author.profile.avatar:
                return obj.author.profile.avatar.url
        except:
            pass
        return None


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_avatar = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ('id', 'author', 'author_username', 'author_avatar', 'image', 
                  'caption', 'likes_count', 'comments_count', 'is_liked', 
                  'comments', 'created_at', 'updated_at')
        read_only_fields = ('author', 'created_at', 'updated_at')
    
    def get_author_avatar(self, obj):
        """Safely get author avatar URL"""
        try:
            if hasattr(obj.author, 'profile') and obj.author.profile.avatar:
                return obj.author.profile.avatar.url
        except:
            pass
        return None
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comments.count()
    
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return request.user in obj.likes.all()
        return False


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'caption')


class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    user_avatar = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(read_only=True)
    is_viewed = serializers.SerializerMethodField()
    
    class Meta:
        model = Story
        fields = ('id', 'user', 'username', 'user_avatar', 'image', 'video',
                  'is_active', 'is_viewed', 'created_at', 'expires_at')
        read_only_fields = ('user', 'created_at', 'expires_at')
    
    def get_user_avatar(self, obj):
        """Safely get user avatar URL"""
        try:
            if hasattr(obj.user, 'profile') and obj.user.profile.avatar:
                return obj.user.profile.avatar.url
        except:
            pass
        return None
    
    def get_is_viewed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return StoryView.objects.filter(story=obj, viewer=request.user).exists()
        return False


class StoryViewSerializer(serializers.ModelSerializer):
    viewer = UserSerializer(read_only=True)
    
    class Meta:
        model = StoryView
        fields = ('id', 'story', 'viewer', 'viewed_at')
        read_only_fields = ('viewer', 'viewed_at')
