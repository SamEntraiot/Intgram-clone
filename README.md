# Instagram Clone - Full Stack Social Media Application

A feature-rich Instagram clone built with Django REST Framework (backend) and vanilla JavaScript (frontend).

## 🚀 Features Implemented

### 1. User Authentication & Profile
- ✅ User registration and login with JWT authentication
- ✅ View and edit user profile (avatar, bio, website)
- ✅ View other users' profiles
- ✅ Display posts count, followers count, following count

### 2. Posts Management
- ✅ Create posts with image upload and caption
- ✅ View post details with likes and comments
- ✅ Like/unlike posts
- ✅ Comment on posts
- ✅ Delete own posts
- ✅ View posts in grid layout on profile

### 3. Feed (Homepage)
- ✅ Display posts from followed users
- ✅ Chronological order (newest first)
- ✅ Infinite scroll pagination
- ✅ Real-time like and comment functionality

### 4. Follow System
- ✅ Follow/unfollow users
- ✅ Automatic follower/following count updates
- ✅ Follow notifications

### 5. Search & Explore
- ✅ Search users by username
- ✅ Explore page with random posts
- ✅ Discover new content

### 6. Stories (24-hour)
- ✅ Upload image/video stories
- ✅ Auto-expire after 24 hours
- ✅ View stories from followed users
- ✅ Track story views

### 7. Messaging System
- ✅ One-on-one conversations
- ✅ Real-time message updates
- ✅ Message preview in conversation list
- ✅ Create new conversations

### 8. Notifications
- ✅ Like notifications
- ✅ Comment notifications
- ✅ Follow notifications
- ✅ Mark all as read functionality
- ✅ Unread badge counter

### 9. Responsive UI/UX
- ✅ Mobile-first CSS design
- ✅ Instagram-inspired interface
- ✅ Responsive navbar with icons
- ✅ Modern modal dialogs
- ✅ Smooth animations and transitions

## 🛠️ Technology Stack

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database
- **Pillow** - Image processing
- **JWT** - Authentication
- **Django Signals** - Automated notifications

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (mobile-first, flexbox, grid)
- **Vanilla JavaScript** - Interactivity
- **Font Awesome** - Icons
- **Fetch API** - AJAX requests

## 📋 API Endpoints

### Authentication
```
POST   /api/register/              - Register new user
POST   /api/login/                 - Login and get JWT token
POST   /api/token/refresh/         - Refresh JWT token
```

### Profile
```
GET    /api/profile/me/            - Get current user profile
PATCH  /api/profile/me/            - Update current user profile
GET    /api/profile/<username>/    - Get user profile by username
POST   /api/profile/<username>/follow/ - Follow/unfollow user
```

### Posts
```
GET    /api/posts/                 - List all posts
POST   /api/posts/                 - Create new post
GET    /api/posts/<id>/            - Get post details
DELETE /api/posts/<id>/            - Delete post (owner only)
POST   /api/posts/<id>/like/       - Toggle like on post
GET    /api/posts/<id>/comments/   - List comments
POST   /api/posts/<id>/comments/   - Add comment
GET    /api/posts/user/<username>/ - Get user's posts
```

### Feed & Explore
```
GET    /api/feed/                  - Get feed from followed users
GET    /api/explore/               - Get explore posts (random)
```

### Stories
```
GET    /api/stories/               - List active stories
POST   /api/stories/               - Create story
GET    /api/stories/<id>/          - View story (marks as viewed)
DELETE /api/stories/<id>/          - Delete story (owner only)
```

### Notifications
```
GET    /api/notifications/         - List notifications
PATCH  /api/notifications/read/    - Mark all as read
```

### Messages
```
GET    /api/conversations/         - List conversations
POST   /api/conversations/create/  - Create conversation
GET    /api/conversations/<id>/    - Get conversation details
GET    /api/conversations/<id>/messages/ - List messages
POST   /api/conversations/<id>/messages/ - Send message
```

### Search
```
GET    /api/search/?q=<query>      - Search users
```

## 🚦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Step-by-Step Installation

1. **Clone or navigate to project directory**
   ```bash
   cd "c:/Users/Nisha/Desktop/instgram clone"
   ```

2. **Activate virtual environment**
   ```bash
   .venv\Scripts\activate
   ```

3. **Install dependencies** (already done)
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations** (already done)
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Frontend: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - API Root: http://localhost:8000/api/

## 📱 Usage Guide

### Getting Started

1. **Register an Account**
   - Visit http://localhost:8000/login
   - Click "Sign up"
   - Fill in email, username, and password
   - Login with your credentials

2. **Setup Your Profile**
   - Click the profile icon in navbar
   - Click "Edit Profile"
   - Upload avatar, add bio, and website
   - Save changes

3. **Create Your First Post**
   - Click the + icon in navbar
   - Upload an image
   - Add a caption (optional)
   - Click "Share"

4. **Explore and Connect**
   - Use search to find users
   - Visit the Explore page for random posts
   - Follow users you like
   - Like and comment on posts

5. **View Your Feed**
   - Click the Home icon
   - See posts from users you follow
   - Scroll for more posts (infinite scroll)

6. **Use Stories**
   - Click + to create a story
   - View stories at the top of feed
   - Stories expire after 24 hours

7. **Send Messages**
   - Click the Messages icon
   - Start a new conversation
   - Send direct messages to users

## 🗂️ Project Structure

```
instgram clone/
├── accounts/               # User accounts & profile app
│   ├── models.py          # Profile, Notification, Conversation, Message
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── template_views.py  # Frontend template views
│   ├── urls.py            # API URL patterns
│   └── admin.py           # Admin configurations
├── posts/                 # Posts & stories app
│   ├── models.py          # Post, Comment, Story, StoryView
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── signals.py         # Notification signals
│   ├── urls.py            # API URL patterns
│   └── admin.py           # Admin configurations
├── socialapp/             # Main project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI configuration
├── templates/             # Frontend HTML templates
│   ├── base.html          # Base template with navbar
│   ├── index.html         # Feed/home page
│   ├── login.html         # Login/register page
│   ├── profile.html       # User profile page
│   ├── explore.html       # Explore page
│   ├── messages.html      # Messages page
│   └── notifications.html # Notifications page
├── media/                 # User uploaded files
│   ├── avatars/           # Profile pictures
│   ├── posts/             # Post images
│   └── stories/           # Story media
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 🔧 Key Implementation Details

### Models

**Profile Model**
- One-to-one with User
- ManyToMany self-reference for following/followers
- Computed properties for counts

**Post Model**
- Foreign key to User (author)
- ManyToMany for likes
- Image upload field

**Story Model**
- Auto-expiring (expires_at field)
- Supports image/video
- 24-hour lifecycle

**Notification Model**
- Generic target (target_type, target_id)
- Created via signals

### Signals

**Like Notification**
- Triggered on post like (M2M changed)
- Creates notification for post author

**Comment Notification**
- Triggered on comment creation
- Creates notification for post author

**Follow Notification**
- Created manually in follow view

### Authentication

- JWT tokens (access + refresh)
- Stored in localStorage
- Sent in Authorization header
- 7-day access token lifetime

### Frontend Architecture

- SPA-like experience with vanilla JS
- API communication via Fetch
- No page reloads for main actions
- Responsive design (mobile-first)

## 🎨 Design Choices

1. **Mobile-First CSS** - Designed for mobile, scales up to desktop
2. **Instagram UI Clone** - Familiar interface for users
3. **RESTful API** - Clean, predictable endpoints
4. **Signal-Based Notifications** - Automatic, decoupled
5. **Infinite Scroll** - Better UX for feed browsing
6. **Modal Dialogs** - Modern UI patterns

## 🐛 Known Limitations

1. No real-time WebSocket support (messages poll every 3s)
2. Stories don't support video playback UI
3. No image filters or editing
4. Simple random explore algorithm
5. No hashtags or tagging system

## 🔜 Future Enhancements

- [ ] WebSocket support for real-time messaging
- [ ] Video posts and IGTV
- [ ] Reels/short videos
- [ ] Hashtags and search by tags
- [ ] User tagging in posts
- [ ] Post sharing
- [ ] Email notifications
- [ ] Password reset functionality
- [ ] Two-factor authentication
- [ ] Advanced search filters
- [ ] Archived posts
- [ ] Multiple image posts (carousel)

## 📝 Development Notes

### Testing the Application

1. Create multiple user accounts
2. Follow users from different accounts
3. Create posts, stories
4. Test likes, comments
5. Send messages between users
6. Check notifications

### Admin Panel Features

Access at http://localhost:8000/admin/

- Manage users and profiles
- View all posts and comments
- Monitor stories
- Check notifications
- View conversations and messages

## 🤝 Contributing

This is a learning project. Feel free to:
- Report bugs
- Suggest features
- Submit improvements

## 📄 License

This project is for educational purposes.

## 👨‍💻 Developer

Built as a full-stack Instagram clone demonstration project.

---

**Happy Coding! 🎉**
