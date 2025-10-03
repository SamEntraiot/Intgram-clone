# 📝 Command Cheatsheet

Quick reference for all common commands.

---

## 🚀 Setup Commands

### Initial Setup
```bash
# Navigate to project
cd "c:\Users\Nisha\Desktop\instgram clone"

# Install dependencies
pip install -r requirements.txt

# Create/apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

---

## 🔧 Development Commands

### Running the Server
```bash
# Standard development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### Database Operations
```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migrations
python manage.py showmigrations

# Reset database (WARNING: deletes data)
python manage.py flush

# Open database shell
python manage.py dbshell
```

### Django Shell
```bash
# Open Python shell with Django
python manage.py shell
```

**Example shell commands:**
```python
# Import models
from django.contrib.auth.models import User
from accounts.models import Profile
from posts.models import Post, Story

# Create test user
user = User.objects.create_user('testuser', 'test@example.com', 'password123')

# Get all users
users = User.objects.all()

# Get user profile
profile = User.objects.get(username='testuser').profile

# Create post
post = Post.objects.create(author=user, caption='Test post', image='path/to/image.jpg')

# Get all posts
posts = Post.objects.all()

# Follow user
user1.profile.following.add(user2.profile)

# Exit shell
exit()
```

---

## 👤 User Management

### Create Superuser
```bash
python manage.py createsuperuser
```

### Change User Password
```bash
python manage.py changepassword <username>
```

### Create Test Users (via shell)
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User

for i in range(1, 6):
    User.objects.create_user(
        username=f'user{i}',
        email=f'user{i}@test.com',
        password='testpass123'
    )
print("Created 5 test users")
```

---

## 📁 Static & Media Files

### Collect Static Files (for production)
```bash
python manage.py collectstatic
```

### Clear Static Files
```bash
python manage.py collectstatic --clear --noinput
```

---

## 🧹 Cleanup Commands

### Clear Cache
```bash
python manage.py clearcache
```

### Remove Migration Files
```bash
# Windows
del /s /q accounts\migrations\0*.py
del /s /q posts\migrations\0*.py

# Then recreate
python manage.py makemigrations
python manage.py migrate
```

### Clear Database (Keep Schema)
```bash
python manage.py flush
```

---

## 🔍 Debugging Commands

### Check for Issues
```bash
python manage.py check
```

### Show All URLs
```bash
python manage.py show_urls
```

### Test Specific App
```bash
python manage.py test accounts
python manage.py test posts
```

### View SQL for Migrations
```bash
python manage.py sqlmigrate accounts 0001
```

---

## 📦 Package Management

### Install New Package
```bash
pip install package-name
pip freeze > requirements.txt
```

### Update Requirements
```bash
pip install -r requirements.txt --upgrade
```

### List Installed Packages
```bash
pip list
```

---

## 🐳 Production Commands

### With Gunicorn (WSGI)
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn socialapp.wsgi:application --bind 0.0.0.0:8000
```

### With Daphne (ASGI - for WebSockets)
```bash
# Already installed in requirements.txt

# Run with daphne
daphne -b 0.0.0.0 -p 8000 socialapp.asgi:application
```

### Environment Variables
```bash
# Windows
set DEBUG=False
set SECRET_KEY=your-secret-key

# Linux/Mac
export DEBUG=False
export SECRET_KEY=your-secret-key
```

---

## 🧪 Testing Commands

### Run All Tests
```bash
python manage.py test
```

### Run Specific Test
```bash
python manage.py test accounts.tests.ProfileTestCase
```

### Run with Coverage
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📊 Data Management

### Export Data (Fixtures)
```bash
# Export all data
python manage.py dumpdata > db.json

# Export specific app
python manage.py dumpdata accounts > accounts.json

# Export specific model
python manage.py dumpdata accounts.Profile > profiles.json
```

### Import Data (Fixtures)
```bash
python manage.py loaddata db.json
```

### Backup Database (SQLite)
```bash
# Windows
copy db.sqlite3 db_backup.sqlite3

# Linux/Mac
cp db.sqlite3 db_backup.sqlite3
```

---

## 🔐 Security Commands

### Generate Secret Key
```bash
python manage.py shell
```
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Change User Email
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
user = User.objects.get(username='username')
user.email = 'newemail@example.com'
user.save()
```

---

## 🌐 API Testing (cURL)

### Register User
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"testuser\",\"email\":\"test@example.com\",\"password\":\"pass123\",\"password2\":\"pass123\"}"
```

### Login
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"testuser\",\"password\":\"pass123\"}"
```

### Get Profile (with token)
```bash
curl -X GET http://localhost:8000/api/profile/me/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Create Post
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "image=@/path/to/image.jpg" \
  -F "caption=Test post"
```

---

## 🔄 Git Commands (If Using Version Control)

```bash
# Initialize git
git init

# Add files
git add .

# Commit
git commit -m "Initial commit - Instagram clone complete"

# Add remote
git remote add origin https://github.com/username/repo.git

# Push
git push -u origin main
```

---

## 📱 Quick Access URLs

| Page | URL |
|------|-----|
| Homepage/Feed | http://localhost:8000/ |
| Login/Register | http://localhost:8000/login |
| Profile | http://localhost:8000/profile |
| Messages | http://localhost:8000/messages |
| Explore | http://localhost:8000/explore |
| Admin Panel | http://localhost:8000/admin/ |
| API Root | http://localhost:8000/api/ |

---

## 🆘 Emergency Commands

### Kill Process on Port 8000
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

### Reset Admin Password
```bash
python manage.py changepassword admin
```

### Clear All Sessions
```bash
python manage.py clearsessions
```

---

## 💡 Pro Tips

### Create Custom Management Command
Create file: `accounts/management/commands/create_test_data.py`
```python
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create test data'

    def handle(self, *args, **kwargs):
        # Your code here
        self.stdout.write('Test data created!')
```

Run: `python manage.py create_test_data`

### Watch for File Changes (Auto-reload)
```bash
# Django automatically watches for changes when running
python manage.py runserver
```

### Access Django Admin
1. Create superuser: `python manage.py createsuperuser`
2. Visit: http://localhost:8000/admin/
3. Login with superuser credentials

---

## 📚 Additional Resources

- **Django Docs**: https://docs.djangoproject.com/
- **DRF Docs**: https://www.django-rest-framework.org/
- **Django Allauth**: https://django-allauth.readthedocs.io/
- **Channels**: https://channels.readthedocs.io/

---

**Keep this file handy for quick command reference!** 📌
