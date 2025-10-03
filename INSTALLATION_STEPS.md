# 🔧 Installation Steps - Follow in Order

## ⚠️ IMPORTANT: Run These Commands First

### Step 1: Install Dependencies
Before running the server, you MUST install all required packages:

```bash
pip install -r requirements.txt
```

This will install:
- Django 4.2
- Django REST Framework
- **django-allauth** (for Google OAuth) ⭐ NEW
- Pillow (image processing)
- djangorestframework-simplejwt (JWT authentication)
- django-cors-headers (CORS support)
- channels (WebSocket support)
- daphne (ASGI server)

### Step 2: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 4: Start Server
```bash
python manage.py runserver
```

### Step 5: Access Application
Open browser: **http://localhost:8000**

---

## ✅ Verification Checklist

After installation, verify:

- [ ] Can access http://localhost:8000
- [ ] Can see login page at http://localhost:8000/login
- [ ] Can register a new user
- [ ] Can login successfully
- [ ] Google OAuth button appears on login page
- [ ] "Forgot password?" link works

---

## 🚨 Troubleshooting

### Error: "No module named 'allauth'"
**Solution**: You forgot Step 1!
```bash
pip install -r requirements.txt
```

### Error: "No such table: accounts_profile"
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Error: "Port 8000 is already in use"
**Solution**: Kill the process or use different port
```bash
# Kill process (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use different port
python manage.py runserver 8080
```

### Error: "CSRF verification failed"
**Solution**: Clear browser cache and cookies
```bash
Ctrl + Shift + Delete (in browser)
```

---

## 📋 Complete Setup Checklist

1. **Install Python 3.8+** ✅
2. **Navigate to project directory**
   ```bash
   cd "c:\Users\Nisha\Desktop\instgram clone"
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start server**
   ```bash
   python manage.py runserver
   ```

7. **Open browser**
   - Visit: http://localhost:8000
   - Login page: http://localhost:8000/login

8. **Register first account**
   - Click "Sign up"
   - Fill in details
   - Login

9. **Test features**
   - Create a post
   - Edit profile
   - Search users
   - Send messages

10. **Optional: Setup Google OAuth**
    - See [SETUP_GUIDE.md](SETUP_GUIDE.md) → Google OAuth Setup

---

## 🎯 What to Do First

1. **Register an account**
2. **Upload profile picture**
3. **Create your first post**
4. **Try the explore page**
5. **Search for users** (if you created test users)

---

## 📚 Next Steps

- **Read**: [FEATURES_CHECKLIST.md](FEATURES_CHECKLIST.md) for all features
- **Setup Google OAuth** (optional): [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Commands Reference**: [COMMANDS.md](COMMANDS.md)

---

## 🎉 You're Ready!

Once you complete these steps, you'll have a fully functional Instagram clone with:

✅ Authentication (with Google OAuth + Password Reset)
✅ User Profiles
✅ Posts (Create, Like, Comment, Delete)
✅ Feed
✅ Follow System
✅ Search & Explore
✅ 24-hour Stories
✅ Real-time Messaging
✅ Notifications
✅ Instagram-like UI (Mobile-responsive)

**Enjoy your Instagram clone!** 🚀
