from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.template_views import (
    index_view, login_view, profile_view, explore_view,
    messages_view, notifications_view, post_detail_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', include('accounts.urls')),
    path('api/', include('posts.urls')),
    
    # Frontend pages
    path('', index_view, name='index'),
    path('login', login_view, name='login'),
    path('explore', explore_view, name='explore'),
    path('messages', messages_view, name='messages'),
    path('notifications', notifications_view, name='notifications'),
    path('post/<int:post_id>', post_detail_view, name='post-detail'),
    path('profile', profile_view, name='my-profile-page'),
    path('profile/<str:username>', profile_view, name='profile-page'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
