# 🚀 Quick Start Guide

Get your Instagram clone running in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Setup Database

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 3: Create Admin Account

```bash
python manage.py createsuperuser
```

Enter username, email, and password when prompted.

## Step 4: Start Server

```bash
python manage.py runserver
```

## Step 5: Open Browser

Visit: **http://localhost:8000**

---

## ✅ What Works Immediately

### Without Configuration:
- ✅ User registration & login
- ✅ Create posts with images
- ✅ Like & comment on posts
- ✅ Follow/unfollow users
- ✅ User profiles
- ✅ Feed from followed users
- ✅ Search users
- ✅ Explore posts
- ✅ 24-hour stories
- ✅ Real-time messaging
- ✅ Notifications
- ✅ Password reset (emails in console)

### Requires Setup (Optional):
- ⚙️ Google OAuth Login - See `SETUP_GUIDE.md` Section "Google OAuth Setup"
- ⚙️ Production Email (Gmail) - See `SETUP_GUIDE.md` Section "Email Configuration"

---

## 🎯 First Steps After Starting

1. **Go to http://localhost:8000/login**
2. Click "Sign up" and create your account
3. Upload a profile picture
4. Create your first post
5. Search for other users and follow them
6. Check out the explore page

---

## 📱 Key Features

| Feature | Description |
|---------|-------------|
| 🔐 **Authentication** | Register, login, Google OAuth, password reset |
| 👤 **Profiles** | Avatar, bio, website, edit profile |
| 📸 **Posts** | Upload images, captions, like, comment, delete |
| 📰 **Feed** | See posts from people you follow |
| 👥 **Follow System** | Follow/unfollow, followers/following lists |
| 🔍 **Search** | Find users by username |
| 🌐 **Explore** | Discover new posts and users |
| 📖 **Stories** | 24-hour disappearing content |
| 💬 **Messaging** | One-to-one real-time chat |
| 🔔 **Notifications** | Like, comment, follow alerts |

---

## 🐛 Quick Troubleshooting

### Server won't start?
```bash
# Make sure you're in the project directory
cd "c:\Users\Nisha\Desktop\instgram clone"

# Check if port 8000 is available
# On Windows: netstat -ano | findstr :8000
```

### Can't login?
- Make sure you created an account at http://localhost:8000/login
- Check username and password are correct
- Look for error messages in the browser console (F12)

### Images not uploading?
- Check that the `media` folder exists
- Ensure you have write permissions
- Try a smaller image file (< 5MB)

### Need help?
Check the detailed `SETUP_GUIDE.md` for comprehensive documentation.

---

## 🎨 Create Test Data (Optional)

To quickly test with multiple users:

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User

# Create 5 test users
for i in range(1, 6):
    User.objects.create_user(
        username=f'user{i}',
        email=f'user{i}@test.com',
        password='password123'
    )
    print(f"Created user{i}")
```

Now you can login as `user1`, `user2`, etc. with password `password123`

---

## 📚 Documentation

- **Full Setup**: `SETUP_GUIDE.md`
- **Features List**: `FEATURES_CHECKLIST.md`
- **API Docs**: See `SETUP_GUIDE.md` → API Endpoints section
- **WebSocket Setup**: `WEBSOCKET_SETUP.md`

---

## 🎉 You're Ready!

Your Instagram clone is running with ALL 10 features:

1. ✅ Authentication (with Google OAuth + Password Reset)
2. ✅ User Profiles
3. ✅ Posts (Create, Like, Comment, Delete)
4. ✅ Feed (Homepage)
5. ✅ Follow System
6. ✅ Search & Explore
7. ✅ Stories (24-hour)
8. ✅ Messaging (Real-time)
9. ✅ Notifications
10. ✅ Instagram-like UI (Mobile-responsive)

**Enjoy your Instagram clone!** 🚀
