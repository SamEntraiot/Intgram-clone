# 🚀 Quick Start Guide

## Start the Application in 3 Steps

### Step 1: Create a Superuser
```bash
.venv\Scripts\python.exe manage.py createsuperuser
```
- Enter username (e.g., `admin`)
- Enter email (e.g., `admin@example.com`)
- Enter password (e.g., `admin123`)

### Step 2: Start the Development Server
```bash
.venv\Scripts\python.exe manage.py runserver
```

### Step 3: Open Your Browser
Visit: **http://localhost:8000/**

---

## 🎯 First Time Usage

### Option A: Create Your Own Account
1. Go to http://localhost:8000/login
2. Click "Sign up"
3. Fill in the registration form
4. Start using the app!

### Option B: Use Admin Account
1. Login with the superuser credentials you created
2. Go to profile and set it up
3. Create some posts

### Option C: Generate Test Data (Recommended)
```bash
.venv\Scripts\python.exe manage.py shell < create_test_data.py
```

This creates 5 test users:
- **john_doe** / password123
- **jane_smith** / password123
- **bob_wilson** / password123
- **alice_brown** / password123
- **charlie_davis** / password123

---

## 📋 What You Can Do

### ✅ Already Working Features

1. **Authentication**
   - Register new account
   - Login/logout
   - JWT token authentication

2. **Profile Management**
   - View your profile
   - Edit profile (avatar, bio, website)
   - View other users' profiles
   - See post/follower/following counts

3. **Posts**
   - Create posts with images
   - Like/unlike posts
   - Comment on posts
   - Delete your own posts
   - View posts in grid on profile

4. **Feed**
   - See posts from people you follow
   - Infinite scroll
   - Real-time likes and comments

5. **Follow System**
   - Follow/unfollow users
   - See who follows you
   - Track following count

6. **Stories**
   - Create 24-hour stories
   - View stories from followed users
   - Stories auto-expire

7. **Search & Explore**
   - Search users by username
   - Explore random posts
   - Discover new content

8. **Messages**
   - Send direct messages
   - Create conversations
   - Real-time message updates

9. **Notifications**
   - Get notified on likes
   - Get notified on comments
   - Get notified on new followers
   - Mark all as read

---

## 🔑 Important URLs

| Page | URL |
|------|-----|
| Home/Feed | http://localhost:8000/ |
| Login | http://localhost:8000/login |
| Profile | http://localhost:8000/profile |
| Explore | http://localhost:8000/explore |
| Messages | http://localhost:8000/messages |
| Notifications | http://localhost:8000/notifications |
| Admin Panel | http://localhost:8000/admin/ |
| API Docs | See README.md |

---

## 🛠️ Admin Panel Access

1. Go to http://localhost:8000/admin/
2. Login with superuser credentials
3. Manage:
   - Users and profiles
   - Posts and comments
   - Stories
   - Notifications
   - Messages

---

## 💡 Tips

1. **Create Multiple Accounts** - Test following/followers features
2. **Upload Images** - JPEG/PNG files work best
3. **Try Mobile View** - Responsive design works on all devices
4. **Use DevTools** - Open browser console to see API calls
5. **Check Admin** - View all data in Django admin panel

---

## 🐛 Troubleshooting

### Server won't start?
```bash
# Make sure you're in the right directory
cd "c:/Users/Nisha/Desktop/instgram clone"

# Activate virtual environment
.venv\Scripts\activate

# Try running migrations again
python manage.py migrate
```

### Can't login?
- Make sure you created a user account
- Check username/password spelling
- Try creating a new account

### Images not showing?
- Check if media folder exists
- Make sure DEBUG=True in settings.py
- Verify file was uploaded successfully

### API errors?
- Open browser DevTools (F12)
- Check Console tab for errors
- Check Network tab for failed requests

---

## 📞 Need Help?

Check these in order:
1. Read the error message carefully
2. Check browser console (F12)
3. Check server terminal output
4. Review README.md for details
5. Check Django admin panel

---

## 🎉 Have Fun!

Start by:
1. Creating an account
2. Setting up your profile
3. Creating your first post
4. Following some users
5. Exploring content

**Enjoy your Instagram clone!** 🚀
