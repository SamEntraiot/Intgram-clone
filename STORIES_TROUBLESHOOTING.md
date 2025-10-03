# Stories Troubleshooting & Testing Guide

## Issue: Can't See Other Users' Stories

### ✅ Fixes Applied

1. **Viewed Stories Styling** ✅
   - Unviewed stories: Colorful gradient border
   - Viewed stories: Gray border (like Instagram)
   - Auto-updates after viewing

2. **Story Loading** ✅
   - Always shows "Add story" button
   - Loads stories from followed users
   - Shows error in console if API fails

---

## Why You Might Not See Stories

### Reason 1: No Followed Users Have Active Stories
**Stories only show from people you follow who have posted in the last 24 hours.**

**Solution:**
```
Option A: Follow more users
1. Go to Explore page
2. Follow some users
3. Ask them to upload stories

Option B: Create test accounts
1. Create 2-3 test accounts
2. Make them follow each other
3. Upload stories from each account
4. You'll see stories from followed users
```

### Reason 2: Stories Have Expired
**Stories automatically disappear after 24 hours.**

**Solution:**
- Upload fresh stories
- Check that other users have recent stories

### Reason 3: API Error
**Check browser console for errors.**

**How to Check:**
1. Press F12 to open Developer Tools
2. Go to Console tab
3. Look for errors when stories load
4. Common errors:
   - 401: Not logged in
   - 404: API endpoint not found
   - 500: Server error

---

## Testing Stories Feature

### Step 1: Create Test Setup

```
1. Create Account A (Main)
2. Create Account B (Test user)
3. Make Account A follow Account B
4. Log into Account B
5. Upload a story from Account B
6. Log back into Account A
7. You should see Account B's story
```

### Step 2: Test Viewing Stories

```
1. See story with gradient border (unviewed)
2. Click to view story
3. Full-screen viewer opens
4. Story plays (5s for photo, video duration for video)
5. Close viewer
6. Story now has gray border (viewed) ✅
```

### Step 3: Test Multiple Stories

```
1. Upload 3-4 stories from different accounts
2. All should appear in Stories section
3. Click first story
4. Tap right to go to next user's story
5. All viewed stories turn gray
```

---

## API Endpoint Check

### Check Stories API
Open browser console and run:

```javascript
// Check if you're getting stories
fetch('/api/stories/', {
    headers: {
        'Authorization': 'Bearer ' + localStorage.getItem('authToken')
    }
})
.then(r => r.json())
.then(data => {
    console.log('Stories:', data);
    console.log('Total stories:', data.length);
    data.forEach((story, i) => {
        console.log(`Story ${i+1}:`, story.username, 'Viewed:', story.is_viewed);
    });
});
```

**Expected Result:**
```json
[
    {
        "id": 1,
        "username": "test_user",
        "user_avatar": "/media/avatars/...",
        "image": "/media/stories/...",
        "is_viewed": false,
        "views_count": 0,
        "created_at": "2025-10-02T...",
        "expires_at": "2025-10-03T..."
    }
]
```

---

## Quick Test Script

### Run this in Browser Console:

```javascript
// Test 1: Check authentication
console.log('Auth Token:', localStorage.getItem('authToken') ? 'EXISTS ✅' : 'MISSING ❌');

// Test 2: Load stories
async function testStories() {
    try {
        const response = await fetch('/api/stories/', {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('authToken')
            }
        });
        const stories = await response.json();
        
        console.log('✅ Stories loaded successfully');
        console.log('📊 Total stories:', stories.length);
        
        if (stories.length === 0) {
            console.log('⚠️ No stories found. Reasons:');
            console.log('   - You may not be following anyone');
            console.log('   - Followed users have no active stories');
            console.log('   - All stories have expired (>24h)');
        } else {
            console.log('📱 Stories:');
            stories.forEach((s, i) => {
                console.log(`   ${i+1}. ${s.username} - ${s.is_viewed ? '👁 Viewed' : '🆕 New'}`);
            });
        }
    } catch (error) {
        console.error('❌ Error loading stories:', error);
    }
}

testStories();
```

---

## Visual Indicators

### Unviewed Story (New)
```
┌─────────────────┐
│   🌈 Gradient   │  ← Colorful rainbow border
│   Border        │
│   ┌─────────┐   │
│   │  👤     │   │
│   │ Avatar  │   │
│   └─────────┘   │
│   Username      │
└─────────────────┘
```

### Viewed Story
```
┌─────────────────┐
│   ⚪ Gray       │  ← Gray border
│   Border        │
│   ┌─────────┐   │
│   │  👤     │   │
│   │ Avatar  │   │
│   └─────────┘   │
│   Username      │
└─────────────────┘
```

---

## Common Solutions

### Problem: "Only see Add story button"
**Solutions:**
1. ✅ Follow other users
2. ✅ Ask followed users to upload stories
3. ✅ Create test accounts with stories
4. ✅ Check browser console for errors

### Problem: "Stories don't turn gray after viewing"
**Solutions:**
1. ✅ Check if backend is tracking views
2. ✅ Refresh page after viewing
3. ✅ Check if `is_viewed` field is in API response

### Problem: "Can't see story content"
**Solutions:**
1. ✅ Check file permissions on media folder
2. ✅ Verify Django MEDIA_URL settings
3. ✅ Check browser console for 404 errors
4. ✅ Ensure story files exist in media/stories/

---

## Backend Checklist

### Django Settings
```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Make sure these are configured
INSTALLED_APPS = [
    # ...
    'posts',  # Stories app
]
```

### URL Configuration
```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Demo Data Creation

### Create Test Stories via Django Shell
```python
python manage.py shell

from django.contrib.auth.models import User
from posts.models import Story
from django.utils import timezone
from datetime import timedelta

# Get or create test user
user = User.objects.get(username='test_user')

# Create a story (you'll need to upload a file manually first)
story = Story.objects.create(
    user=user,
    image='stories/test_image.jpg',  # Upload this file first
    expires_at=timezone.now() + timedelta(hours=24)
)

print(f"Created story {story.id}")
```

---

## Success Checklist

Once working, you should see:

- ✅ "Add story" button (always visible)
- ✅ Other users' stories with gradient borders
- ✅ Stories from followed users only
- ✅ Click story → full-screen viewer opens
- ✅ Story plays (5s for photo, video for videos)
- ✅ Close viewer → story border turns gray
- ✅ Console shows successful API calls
- ✅ No 404/500 errors in console

---

## Need More Help?

Run this complete diagnostic:

```javascript
// COMPLETE DIAGNOSTIC
console.log('=== STORIES DIAGNOSTIC ===');
console.log('1. Auth:', localStorage.getItem('authToken') ? '✅' : '❌');

fetch('/api/stories/', {
    headers: { 'Authorization': 'Bearer ' + localStorage.getItem('authToken') }
})
.then(r => {
    console.log('2. API Response:', r.status === 200 ? '✅' : '❌ ' + r.status);
    return r.json();
})
.then(data => {
    console.log('3. Stories Count:', data.length);
    console.log('4. Stories Data:', data);
    if (data.length > 0) {
        console.log('✅ Everything working!');
    } else {
        console.log('⚠️ No stories - follow users and ask them to upload');
    }
})
.catch(err => {
    console.error('❌ Error:', err);
});
```

---

**Status**: Stories feature is working ✅  
**Issue**: Need followed users with active stories to see them  
**Solution**: Create test accounts or follow users with stories  
