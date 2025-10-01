# 🧪 API Testing Guide

Quick reference for testing all API endpoints.

## 🔑 Authentication First

### Register a New User
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password2": "testpass123"
  }'
```

### Login and Get Token
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Save the access token for subsequent requests!**

---

## 👤 Profile Endpoints

### Get My Profile
```bash
curl http://localhost:8000/api/profile/me/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Update My Profile
```bash
curl -X PATCH http://localhost:8000/api/profile/me/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "bio=Hello World! 🌍" \
  -F "website=https://example.com"
```

### View Another User's Profile
```bash
curl http://localhost:8000/api/profile/john_doe/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Follow/Unfollow User
```bash
curl -X POST http://localhost:8000/api/profile/john_doe/follow/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 📸 Post Endpoints

### Create a Post
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "image=@/path/to/image.jpg" \
  -F "caption=My first post! 🎉"
```

### Get All Posts
```bash
curl http://localhost:8000/api/posts/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get Single Post
```bash
curl http://localhost:8000/api/posts/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Like/Unlike Post
```bash
curl -X POST http://localhost:8000/api/posts/1/like/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Add Comment
```bash
curl -X POST http://localhost:8000/api/posts/1/comments/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Great post! 👍"
  }'
```

### Delete Post (Owner Only)
```bash
curl -X DELETE http://localhost:8000/api/posts/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get User's Posts
```bash
curl http://localhost:8000/api/posts/user/john_doe/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 📰 Feed & Explore

### Get Feed (Following Users)
```bash
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get Feed with Pagination
```bash
curl http://localhost:8000/api/feed/?page=2 \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Explore Posts
```bash
curl http://localhost:8000/api/explore/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 📖 Story Endpoints

### Get Active Stories
```bash
curl http://localhost:8000/api/stories/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Create Story
```bash
curl -X POST http://localhost:8000/api/stories/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -F "image=@/path/to/story.jpg"
```

### View Story (Marks as Viewed)
```bash
curl http://localhost:8000/api/stories/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Delete Story (Owner Only)
```bash
curl -X DELETE http://localhost:8000/api/stories/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 🔔 Notification Endpoints

### Get All Notifications
```bash
curl http://localhost:8000/api/notifications/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Mark All as Read
```bash
curl -X PATCH http://localhost:8000/api/notifications/read/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 💬 Messaging Endpoints

### Get All Conversations
```bash
curl http://localhost:8000/api/conversations/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Create New Conversation
```bash
curl -X POST http://localhost:8000/api/conversations/create/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe"
  }'
```

### Get Conversation Details
```bash
curl http://localhost:8000/api/conversations/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Get Messages in Conversation
```bash
curl http://localhost:8000/api/conversations/1/messages/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Send Message
```bash
curl -X POST http://localhost:8000/api/conversations/1/messages/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello! How are you?"
  }'
```

---

## 🔍 Search Endpoint

### Search Users
```bash
curl "http://localhost:8000/api/search/?q=john" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 🔄 Token Refresh

### Refresh Access Token
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "YOUR_REFRESH_TOKEN"
  }'
```

---

## 🧪 Testing with Python

```python
import requests

# Base URL
BASE_URL = "http://localhost:8000/api"

# 1. Register
response = requests.post(f"{BASE_URL}/register/", json={
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password2": "testpass123"
})
print("Register:", response.json())

# 2. Login
response = requests.post(f"{BASE_URL}/login/", json={
    "username": "testuser",
    "password": "testpass123"
})
token = response.json()["access"]
print("Token:", token)

# 3. Get Profile
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{BASE_URL}/profile/me/", headers=headers)
print("Profile:", response.json())

# 4. Create Post
files = {"image": open("test.jpg", "rb")}
data = {"caption": "Test post"}
response = requests.post(f"{BASE_URL}/posts/", headers=headers, files=files, data=data)
print("Post created:", response.json())

# 5. Get Feed
response = requests.get(f"{BASE_URL}/feed/", headers=headers)
print("Feed:", response.json())
```

---

## 🧪 Testing with JavaScript (Browser Console)

```javascript
const BASE_URL = 'http://localhost:8000/api';
let token = '';

// 1. Register
fetch(`${BASE_URL}/register/`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'testuser',
    email: 'test@example.com',
    password: 'testpass123',
    password2: 'testpass123'
  })
})
.then(r => r.json())
.then(data => console.log('Register:', data));

// 2. Login
fetch(`${BASE_URL}/login/`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'testuser',
    password: 'testpass123'
  })
})
.then(r => r.json())
.then(data => {
  token = data.access;
  console.log('Token:', token);
});

// 3. Get Profile
fetch(`${BASE_URL}/profile/me/`, {
  headers: { 'Authorization': `Bearer ${token}` }
})
.then(r => r.json())
.then(data => console.log('Profile:', data));

// 4. Get Feed
fetch(`${BASE_URL}/feed/`, {
  headers: { 'Authorization': `Bearer ${token}` }
})
.then(r => r.json())
.then(data => console.log('Feed:', data));
```

---

## ✅ Testing Checklist

### Authentication
- [ ] Register new user
- [ ] Login with credentials
- [ ] Refresh token
- [ ] Access protected endpoint with token

### Profile
- [ ] View own profile
- [ ] Update profile (bio, website)
- [ ] Upload avatar
- [ ] View another user's profile
- [ ] Follow/unfollow user

### Posts
- [ ] Create post with image
- [ ] View all posts
- [ ] View single post
- [ ] Like/unlike post
- [ ] Add comment
- [ ] Delete own post
- [ ] View user's posts

### Feed & Explore
- [ ] View feed (following users)
- [ ] Pagination works
- [ ] Explore random posts

### Stories
- [ ] Create story
- [ ] View active stories
- [ ] Story marks as viewed
- [ ] Delete own story

### Notifications
- [ ] Receive like notification
- [ ] Receive comment notification
- [ ] Receive follow notification
- [ ] Mark all as read

### Messaging
- [ ] Create conversation
- [ ] Send message
- [ ] Receive message
- [ ] View conversation list

### Search
- [ ] Search users by username
- [ ] Case-insensitive search works

---

## 🐛 Common Issues

### 401 Unauthorized
- Token expired or invalid
- Solution: Login again to get new token

### 403 Forbidden
- Trying to delete/edit someone else's content
- Solution: Only owners can modify their content

### 400 Bad Request
- Missing required fields
- Invalid data format
- Solution: Check request body matches expected format

### 404 Not Found
- Resource doesn't exist
- Wrong URL
- Solution: Verify ID and endpoint

---

## 📊 Expected Response Formats

### Profile Response
```json
{
  "id": 1,
  "user": 1,
  "username": "testuser",
  "email": "test@example.com",
  "avatar": "/media/avatars/avatar.jpg",
  "bio": "Hello World!",
  "website": "https://example.com",
  "posts_count": 5,
  "followers_count": 10,
  "following_count": 15,
  "is_following": false,
  "created_at": "2025-10-01T10:00:00Z",
  "updated_at": "2025-10-01T10:00:00Z"
}
```

### Post Response
```json
{
  "id": 1,
  "author": {...},
  "author_username": "testuser",
  "author_avatar": "/media/avatars/avatar.jpg",
  "image": "/media/posts/post.jpg",
  "caption": "My first post!",
  "likes_count": 10,
  "comments_count": 5,
  "is_liked": false,
  "comments": [...],
  "created_at": "2025-10-01T10:00:00Z",
  "updated_at": "2025-10-01T10:00:00Z"
}
```

---

**Happy Testing! 🚀**
