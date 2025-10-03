# Instagram Clone - Complete Setup Guide

This is a full-featured Instagram clone built with Django REST Framework and vanilla JavaScript. All 10 required features are implemented and ready to use.

## ✅ Implemented Features

### 1. Authentication ✅
- ✅ User Registration (username/email/password)
- ✅ User Login/Logout with JWT tokens
- ✅ Google OAuth Login
- ✅ Profile creation (auto-created on signup)
- ✅ Password reset via email

### 2. User Profile ✅
- ✅ View own profile (posts, followers, following count)
- ✅ Edit profile (name, bio, profile picture, website)
- ✅ View other users' profiles

### 3. Posts ✅
- ✅ Create post (upload image + caption)
- ✅ Like/unlike posts
- ✅ Comment on posts
- ✅ Delete own posts

### 4. Feed (Homepage) ✅
- ✅ Show posts from followed users (latest first)
- ✅ Like & comment directly from feed
- ✅ Infinite scroll pagination

### 5. Follow System ✅
- ✅ Follow/unfollow users
- ✅ Display followers & following lists
- ✅ Remove followers
- ✅ User suggestions

### 6. Search & Explore ✅
- ✅ Search users by username
- ✅ Explore tab with recommended posts

### 7. Stories ✅
- ✅ Add 24-hour disappearing stories
- ✅ View others' stories
- ✅ Story views tracking

### 8. Messaging ✅
- ✅ One-to-one chat (real-time with WebSockets)
- ✅ Last message preview
- ✅ Unread message count
- ✅ Message read status

### 9. Notifications ✅
- ✅ Like notifications
- ✅ Comment notifications
- ✅ Follow notifications
- ✅ Real-time updates

### 10. UI/UX ✅
- ✅ Instagram-like clean layout
- ✅ Mobile-responsive design
- ✅ Modern UI with smooth animations

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

---

## 🚀 Installation Steps

### 1. Clone or Navigate to the Project

```bash
cd "c:\Users\Nisha\Desktop\instgram clone"
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://localhost:8000**

---

## 🔧 Configuration

### Google OAuth Setup (Optional)

To enable Google login:

1. **Go to Google Cloud Console**: https://console.cloud.google.com/

2. **Create a new project** (or select existing)

3. **Enable Google+ API**:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google+ API" and enable it

4. **Create OAuth 2.0 Credentials**:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Application type: Web application
   - Authorized redirect URIs: 
     - `http://localhost:8000/accounts/google/login/callback/`
     - `http://127.0.0.1:8000/accounts/google/login/callback/`

5. **Copy Client ID and Secret**

6. **Update settings.py**:
   ```python
   SOCIALACCOUNT_PROVIDERS = {
       'google': {
           'APP': {
               'client_id': 'YOUR_GOOGLE_CLIENT_ID',
               'secret': 'YOUR_GOOGLE_CLIENT_SECRET',
               'key': ''
           }
       }
   }
   ```

7. **Register the app in Django Admin**:
   - Go to http://localhost:8000/admin/
   - Navigate to "Sites" > "example.com" and change to `localhost:8000`
   - Navigate to "Social applications" > "Add social application"
   - Provider: Google
   - Name: Google OAuth
   - Client id: (paste your client ID)
   - Secret key: (paste your secret)
   - Sites: Select "localhost:8000"
   - Save

### Email Configuration (For Password Reset)

For development, emails are printed to the console. For production:

**Update settings.py**:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use App Password for Gmail
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

**Gmail App Password**: 
- Go to Google Account Settings
- Security > 2-Step Verification > App passwords
- Generate a new app password for "Mail"

---

## 📁 Project Structure

```
instgram-clone/
├── accounts/              # User authentication, profiles, messaging
│   ├── models.py         # Profile, Notification, Message, Conversation
│   ├── views.py          # API endpoints
│   ├── serializers.py    # REST serializers
│   └── urls.py           # API routes
├── posts/                # Posts, comments, stories
│   ├── models.py         # Post, Comment, Story, StoryView
│   ├── views.py          # API endpoints
│   └── urls.py           # API routes
├── templates/            # Frontend HTML templates
│   ├── index.html        # Feed/Homepage
│   ├── login.html        # Login/Register
│   ├── profile.html      # User profiles
│   ├── messages.html     # Messaging
│   ├── explore.html      # Explore page
│   ├── reset_password.html  # Password reset
│   └── ...
├── socialapp/            # Django project settings
│   ├── settings.py       # Configuration
│   ├── urls.py           # Main URL routing
│   └── asgi.py           # WebSocket configuration
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🎯 Usage

### Default URLs

- **Homepage (Feed)**: http://localhost:8000/
- **Login/Register**: http://localhost:8000/login
- **Profile**: http://localhost:8000/profile
- **Messages**: http://localhost:8000/messages
- **Explore**: http://localhost:8000/explore
- **Admin Panel**: http://localhost:8000/admin/

### API Endpoints

#### Authentication
- `POST /api/register/` - User registration
- `POST /api/login/` - Login (returns JWT tokens)
- `POST /api/token/refresh/` - Refresh JWT token
- `POST /api/password-reset/` - Request password reset
- `POST /api/password-reset-confirm/` - Confirm password reset

#### Profiles
- `GET /api/profile/me/` - Get current user profile
- `PATCH /api/profile/me/` - Update profile
- `GET /api/profile/<username>/` - Get user profile
- `POST /api/profile/<username>/follow/` - Follow/unfollow
- `GET /api/profile/<username>/followers/` - Get followers
- `GET /api/profile/<username>/following/` - Get following

#### Posts
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create post
- `GET /api/posts/<id>/` - Get post detail
- `DELETE /api/posts/<id>/` - Delete post
- `POST /api/posts/<id>/like/` - Like/unlike post
- `GET /api/posts/<id>/comments/` - Get comments
- `POST /api/posts/<id>/comments/` - Add comment
- `GET /api/feed/` - Get personalized feed
- `GET /api/explore/` - Get explore posts

#### Stories
- `GET /api/stories/` - Get active stories
- `POST /api/stories/` - Create story
- `GET /api/stories/<id>/` - View story (marks as viewed)
- `DELETE /api/stories/<id>/` - Delete story

#### Messaging
- `GET /api/conversations/` - List conversations
- `POST /api/conversations/create/` - Start conversation
- `GET /api/conversations/<id>/messages/` - Get messages
- `POST /api/conversations/<id>/messages/` - Send message

#### Notifications
- `GET /api/notifications/` - List notifications
- `PATCH /api/notifications/read/` - Mark all as read

#### Search
- `GET /api/search/?q=username` - Search users
- `GET /api/suggestions/` - Get user suggestions

---

## 🧪 Testing

### Create Test Data

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
from accounts.models import Profile

# Create test users
users = []
for i in range(5):
    user = User.objects.create_user(
        username=f'testuser{i}',
        email=f'test{i}@example.com',
        password='testpass123'
    )
    users.append(user)

print("Test users created!")
```

### Test Authentication

```bash
# Login
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser0","password":"testpass123"}'
```

---

## 📱 Features Walkthrough

### 1. Registration & Login
- Go to http://localhost:8000/login
- Click "Sign up" to create an account
- Or click "Log in with Google" for OAuth

### 2. Create Posts
- Click the "+" icon in the navbar
- Upload an image and add a caption
- Post appears in your profile and followers' feeds

### 3. Stories
- Click your profile picture with "+" icon
- Upload story (expires in 24 hours)
- Click on other users' stories to view

### 4. Follow Users
- Search for users in the search bar
- Visit their profile
- Click "Follow" button

### 5. Messaging
- Click the message icon in navbar
- Start a new conversation
- Real-time messaging with WebSockets

### 6. Explore
- Click "Explore" to see posts from all users
- Discover new content and users

---

## 🔒 Security Features

- ✅ JWT authentication
- ✅ Password hashing
- ✅ CSRF protection
- ✅ Secure password reset
- ✅ Input validation
- ✅ Permission checks

---

## 🛠️ Tech Stack

**Backend:**
- Django 4.2
- Django REST Framework
- Django Channels (WebSockets)
- Simple JWT
- django-allauth (OAuth)

**Frontend:**
- Vanilla JavaScript (ES6+)
- HTML5
- CSS3
- Fetch API
- WebSocket API

**Database:**
- SQLite (Development)
- PostgreSQL/MySQL (Production ready)

---

## 🚀 Deployment

### For Production:

1. **Update settings.py**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['your-domain.com']
   ```

2. **Use production database** (PostgreSQL/MySQL)

3. **Configure static files**:
   ```bash
   python manage.py collectstatic
   ```

4. **Set up environment variables** for secrets

5. **Use production ASGI server**:
   ```bash
   daphne -b 0.0.0.0 -p 8000 socialapp.asgi:application
   ```

6. **Set up Redis** for channels layer (WebSockets):
   ```python
   CHANNEL_LAYERS = {
       'default': {
           'BACKEND': 'channels_redis.core.RedisChannelLayer',
           'CONFIG': {
               "hosts": [('127.0.0.1', 6379)],
           },
       },
   }
   ```

---

## 🐛 Troubleshooting

### Issue: Google OAuth not working
- Verify redirect URIs match exactly
- Check that Google+ API is enabled
- Ensure Site domain is correct in Django admin

### Issue: WebSocket connection failed
- Check that Daphne is running (not just runserver)
- Verify ASGI configuration
- Check browser console for errors

### Issue: Images not loading
- Ensure MEDIA_URL and MEDIA_ROOT are configured
- Check file permissions
- Verify static file serving in development

### Issue: Password reset email not sending
- Check EMAIL_BACKEND configuration
- For Gmail, use App Password, not regular password
- Check console output in development mode

---

## 📝 API Authentication

All protected endpoints require JWT authentication:

```javascript
// Login first
const response = await fetch('/api/login/', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({username: 'user', password: 'pass'})
});
const {access} = await response.json();

// Use token for authenticated requests
fetch('/api/profile/me/', {
    headers: {
        'Authorization': `Bearer ${access}`
    }
});
```

---

## 📄 License

This project is for educational purposes.

---

## 🤝 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Review Django logs in the console
3. Check browser console for frontend errors
4. Ensure all migrations are run
5. Verify all dependencies are installed

---

## 🎉 You're All Set!

Your Instagram clone is now fully configured with all 10 features. Start the server and enjoy!

```bash
python manage.py runserver
```

Visit http://localhost:8000 and start exploring! 🚀
