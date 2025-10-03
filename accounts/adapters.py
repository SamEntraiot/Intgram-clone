from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
import re


class CustomAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        """
        Allow both manual and social account signup
        """
        return True
    
    def clean_email(self, email):
        """
        Allow multiple accounts with the same email (like Instagram)
        """
        return email


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        """
        Saves a newly signed up social login. In case of auto-signup,
        the signup form is not available.
        """
        user = sociallogin.user
        
        # Generate username from email or Google name
        if not user.username:
            # Try to get username from Google data
            extra_data = sociallogin.account.extra_data
            
            # First try the email prefix
            if user.email:
                base_username = user.email.split('@')[0]
            # Fallback to Google name
            elif extra_data.get('name'):
                base_username = re.sub(r'[^a-zA-Z0-9_]', '', extra_data['name'].lower())
            else:
                base_username = 'user'
            
            # Ensure username is unique
            username = base_username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            
            user.username = username
        
        # Set first and last name from Google data if available
        extra_data = sociallogin.account.extra_data
        if not user.first_name and extra_data.get('given_name'):
            user.first_name = extra_data['given_name']
        if not user.last_name and extra_data.get('family_name'):
            user.last_name = extra_data['family_name']
        
        user.save()
        return user
    
    def is_auto_signup_allowed(self, request, sociallogin):
        """
        Always allow auto signup for social accounts to bypass the signup form
        """
        return True
    
    def get_connect_redirect_url(self, request, socialaccount):
        """
        Returns the default URL to redirect to after successfully
        connecting a social account.
        """
        # Generate a temporary token for JWT generation
        try:
            if socialaccount.user and socialaccount.user.id:
                from django.core.signing import Signer
                signer = Signer()
                temp_token = signer.sign(socialaccount.user.id)
                return f'/oauth-complete?temp_token={temp_token}'
        except Exception:
            pass
        return '/oauth-complete'
    
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed.
        """
        # Since we allow multiple accounts with same email, 
        # let Django Allauth handle the social login normally
        # without trying to connect to existing users
        pass
    
    def get_signup_form_class(self, request, sociallogin):
        """
        Return None to skip the signup form completely
        """
        return None
    
    def populate_user(self, request, sociallogin, data):
        """
        Populates user information from social provider data
        """
        user = super().populate_user(request, sociallogin, data)
        
        # Ensure user is properly logged in after creation
        if user and not user.pk:
            # This is a new user, make sure they get logged in
            pass
            
        return user
    
    def get_login_redirect_url(self, request):
        """
        Returns the default URL to redirect to after a successful login.
        """
        # Generate a temporary token for JWT generation
        try:
            if request.user and request.user.is_authenticated and request.user.id:
                from django.core.signing import Signer
                signer = Signer()
                temp_token = signer.sign(request.user.id)
                return f'/oauth-complete?temp_token={temp_token}'
        except Exception:
            pass
        return '/oauth-complete'
    
