from django.shortcuts import render
from django.views.generic import TemplateView


def index_view(request):
    """Render the feed/home page"""
    return render(request, 'index.html')


def login_view(request):
    """Render the login/register page"""
    return render(request, 'login.html')


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
    """Render the notifications page"""
    return render(request, 'notifications.html')


def post_detail_view(request, post_id):
    """Render the post detail page"""
    return render(request, 'post_detail.html', {'post_id': post_id})
