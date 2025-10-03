# Video Upload Fix for Posts

## Issue
Users were unable to upload videos when creating new posts. The error was:
```
POST http://127.0.0.1:8000/api/posts/ 400 (Bad Request)
```

## Root Cause
The `Post` model only had an `image` field but the frontend was accepting both images and videos (`accept="image/*,video/*"`). When a video was uploaded, it was being sent with the wrong field name, causing the API to reject it with a 400 Bad Request error.

## Solution

### 1. **Backend Changes**

#### Model Update (`posts/models.py`)
- Added `video` field to `Post` model
- Made both `image` and `video` fields optional (`blank=True, null=True`)
- Posts can now have either an image OR a video

```python
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    video = models.FileField(upload_to='posts/', blank=True, null=True)
    caption = models.TextField(max_length=2200, blank=True)
    # ... other fields
```

#### Serializer Update (`posts/serializers.py`)
- Added `video` field to `PostSerializer` and `PostCreateSerializer`
- Added validation to ensure either image or video is provided (but not both)

```python
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'video', 'caption')
    
    def validate(self, data):
        image = data.get('image')
        video = data.get('video')
        
        if not image and not video:
            raise serializers.ValidationError("Either image or video is required")
        
        if image and video:
            raise serializers.ValidationError("Cannot upload both image and video")
        
        return data
```

#### Database Migration
- Created migration: `posts\migrations\0003_post_video_alter_post_image.py`
- Applied migration successfully

### 2. **Frontend Changes**

#### File Upload Logic (`templates/base.html`)
- Updated file input to properly detect file type (image vs video)
- Sends `image` field for images, `video` field for videos
- Updated preview to show video player for videos

**Preview Handling:**
```javascript
const previewImage = document.getElementById('previewImage');
const previewVideo = document.getElementById('previewVideo');

if (file.type.startsWith('image/')) {
    previewImage.src = fileURL;
    previewImage.style.display = 'block';
    previewVideo.style.display = 'none';
} else if (file.type.startsWith('video/')) {
    previewVideo.src = fileURL;
    previewVideo.style.display = 'block';
    previewImage.style.display = 'none';
}
```

**Form Submission:**
```javascript
const formData = new FormData();

if (file.type.startsWith('image/')) {
    formData.append('image', file);
} else if (file.type.startsWith('video/')) {
    formData.append('video', file);
}

formData.append('caption', caption);
```

#### Display Updates
Updated all templates to display videos when present:

**`index.html` (Feed):**
```javascript
${post.video ? 
    `<video src="${post.video}" class="post-image" controls></video>` :
    `<img src="${post.image}" alt="Post" class="post-image">`
}
```

**`profile.html` (Profile Grid & Detail Modal):**
- Post thumbnails show video preview
- Detail modal shows video player with controls

**`post_detail.html` (Post Detail Page):**
- Shows video player when video is present

**`explore.html` (Explore Page):**
- Explore grid shows video thumbnails

### 3. **UI Improvements**
- Added video preview with controls in create post modal
- Changed "Change photo" button text to "Change media"
- Video thumbnails display in all grid views
- Full video playback with controls in detail views

## How It Works Now

1. **Creating a Post with Video:**
   - User clicks "+ Create" → "New Post"
   - Selects a video file
   - Video preview appears with playback controls
   - User adds caption and clicks "Share"
   - Frontend detects video type and sends as `video` field
   - Backend validates and saves the video post

2. **Viewing Video Posts:**
   - Feed, profile, and explore pages show video thumbnails
   - Click to view shows video player with controls
   - Users can play, pause, seek, and control volume

## Validation
- ✅ Either image or video is required (not both)
- ✅ Empty posts are rejected
- ✅ Both images and videos can be uploaded
- ✅ Videos display correctly across all pages

## Testing
To test video upload:
1. Create a new post
2. Select a video file (MP4, WebM, etc.)
3. Add a caption
4. Click "Share"
5. Video should upload successfully and appear in feed
6. Video should have playback controls

## Files Modified
- `posts/models.py` - Added video field
- `posts/serializers.py` - Added video field and validation
- `templates/base.html` - Updated upload and preview logic
- `templates/index.html` - Video display in feed
- `templates/profile.html` - Video display in grid and modal
- `templates/post_detail.html` - Video display in detail view
- `templates/explore.html` - Video display in explore grid

## Migration Files
- `posts/migrations/0003_post_video_alter_post_image.py`

---

**Status:** ✅ **FIXED** - Video upload now works successfully!
