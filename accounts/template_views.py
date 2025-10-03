from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def index_view(request):
    """Render the feed/home page"""
    return render(request, 'index.html')


def login_view(request):
    """Render the login/register page"""
    return render(request, 'login.html')


def register_view(request):
    """Render the registration page"""
    return render(request, 'register.html')


def profile_view(request, username=None):
    """Render the profile page"""
    return render(request, 'profile.html', {'username': username})


def explore_view(request):
    """Render the explore page"""
    return render(request, 'explore.html')


def messages_view(request):
    """Render the messages page"""
    return render(request, 'messages.html')


def notifications_view(request):
    """Redirect to home page - notifications now work as a side panel"""
    return redirect('/')


def post_detail_view(request, post_id):
    """Render the post detail page"""
    return render(request, 'post_detail.html', {'post_id': post_id})


def reset_password_view(request, uid, token):
    """Render the password reset confirmation page"""
    return render(request, 'reset_password.html', {'uid': uid, 'token': token})


def oauth_complete_view(request):
    """Render the OAuth completion page which swaps session for JWT tokens."""
    return render(request, 'oauth_complete.html')


def social_signup_redirect(request):
    """Redirect social signup directly to oauth complete"""
    return redirect('/oauth-complete')
