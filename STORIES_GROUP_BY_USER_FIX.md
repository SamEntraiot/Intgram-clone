# Stories Grouped By User - FIXED ✅

## Problem

**Before Fix:**
Users with multiple stories appeared multiple times in the Stories section:

```
Stories Section:
[Add story] [sam] [adam] [adam] [sam] [adam] [adam]
```

**Issue:**
- sam posted 2 stories → 2 separate circles
- adam posted 3 stories → 3 separate circles
- Very cluttered and confusing UI
- Not like Instagram behavior

---

## Expected Behavior (Instagram-like)

**After Fix:**
Each user should appear only ONCE, regardless of how many stories they have:

```
Stories Section:
[Add story] [sam] [adam]
             ↓      ↓
          2 stories  3 stories
```

When clicked:
- sam's circle → Shows all 2 stories in sequence
- adam's circle → Shows all 3 stories in sequence

---

## Solution Applied

### 1. Group Stories by Username

Updated `templates/index.html` → `loadStories()` function:

**Before (Each story separate):**
```javascript
const stories = [...]; // Array of all stories

storiesHTML += stories.map(story => {
    return `<div class="story-item" onclick="viewStory(${story.id})">...`;
});
```

**After (Grouped by user):**
```javascript
const stories = [...]; // Array of all stories

// Group stories by username
const groupedStories = {};
stories.forEach(story => {
    const username = story.username || 'Unknown';
    if (!groupedStories[username]) {
        groupedStories[username] = {
            username: username,
            user_avatar: story.user_avatar,
            stories: [],
            is_viewed: true
        };
    }
    groupedStories[username].stories.push(story);
    
    // If any story is not viewed, mark group as not viewed
    if (!story.is_viewed) {
        groupedStories[username].is_viewed = false;
    }
});

// Convert to array
const userStories = Object.values(groupedStories);

storiesHTML += userStories.map(userStory => {
    return `<div class="story-item" onclick="viewUserStories('${userStory.username}', ...)">...`;
});
```

---

### 2. View All User Stories

Added new function `viewUserStories()` in `templates/index.html`:

```javascript
async function viewUserStories(username, firstStoryId) {
    try {
        // Load all stories
        const response = await apiCall('/stories/');
        const allStories = Array.isArray(response) ? response : (response.results || []);
        
        // Filter stories for this specific user
        const userStories = allStories.filter(story => story.username === username);
        
        if (userStories.length > 0) {
            // Open story viewer with ALL user's stories
            openStoryViewerWithStories(userStories);
        }
    } catch (error) {
        console.error('Error loading user stories:', error);
        // Fallback to single story
        openStoryViewer(firstStoryId);
    }
}
```

---

### 3. Story Viewer for Multiple Stories

Added new function `openStoryViewerWithStories()` in `templates/base.html`:

```javascript
function openStoryViewerWithStories(stories) {
    // Open story viewer with multiple stories
    if (!stories || stories.length === 0) return;
    
    currentUserStories = stories;  // Array of all user's stories
    currentStoryIndex = 0;
    
    document.getElementById('storyViewer').classList.add('active');
    displayStory(stories[0]);  // Show first story
}
```

---

## How It Works

### Story Display Flow:

```
1. Load all stories from API
    ↓
2. Group stories by username
    {
      "sam": { username: "sam", stories: [story1, story2] },
      "adam": { username: "adam", stories: [story1, story2, story3] }
    }
    ↓
3. Convert to array and display ONE circle per user
    [sam] [adam]
    ↓
4. User clicks on sam's circle
    ↓
5. viewUserStories("sam") called
    ↓
6. Filter all stories for username = "sam"
    ↓
7. openStoryViewerWithStories([story1, story2])
    ↓
8. Story viewer shows story1 first
    ↓
9. User swipes/taps → shows story2
    ↓
10. After story2 ends → closes viewer
```

---

## Story Viewer Navigation

### Progress Bars:
```
┌─────────────────────────────────┐
│ ▓▓▓▓▓▓▓ ░░░░░░░ ░░░░░░░        │ ← 3 bars for 3 stories
│   sam                      X    │
│                                 │
│       [Story Content]           │
│                                 │
│                                 │
└─────────────────────────────────┘
```

### Navigation:
- **Tap right side** → Next story
- **Tap left side** → Previous story
- **After last story** → Auto close
- **Press Esc** → Close viewer

---

## Visual Comparison

### Before Fix:
```
Stories Section:
┌────────────────────────────────────────────────────────┐
│ [+]  [sam]  [adam]  [adam]  [sam]  [adam]  [adam]     │
│ Add   👤     👤      👤      👤     👤      👤          │
│                                                        │
│ ← 7 items (messy!)                                     │
└────────────────────────────────────────────────────────┘
```

### After Fix:
```
Stories Section:
┌──────────────────────────────────┐
│ [+]  [sam]  [adam]               │
│ Add   👤     👤                   │
│      (2)    (3)  ← story counts  │
│                                  │
│ ← 3 items (clean!)               │
└──────────────────────────────────┘
```

---

## Viewed State Handling

### Logic:
- If **ALL** stories from a user are viewed → Circle shows as "viewed" (grey)
- If **ANY** story from a user is unviewed → Circle shows as "new" (gradient ring)

```javascript
// If any story is not viewed, mark the whole group as not viewed
if (!story.is_viewed) {
    groupedStories[username].is_viewed = false;
}
```

### Visual:
```
[sam]  ← All stories viewed (grey circle)
[adam] ← Has unviewed stories (colored gradient ring)
```

---

## Example Scenario

### Database Has:
```
Stories:
- id: 1, username: "sam", image: "photo1.jpg"
- id: 2, username: "adam", image: "photo2.jpg"
- id: 3, username: "adam", image: "photo3.jpg"
- id: 4, username: "sam", image: "photo4.jpg"
- id: 5, username: "adam", image: "photo5.jpg"
```

### Display Shows:
```
[Add story] [sam] [adam]
             ↓      ↓
          2 stories  3 stories
```

### User Clicks sam:
```
Story Viewer opens with:
- Story 1: photo1.jpg
- Story 2: photo4.jpg

Progress bars: [▓▓▓▓] [░░░░]
                ↑ current
```

### User Clicks adam:
```
Story Viewer opens with:
- Story 1: photo2.jpg
- Story 2: photo3.jpg
- Story 3: photo5.jpg

Progress bars: [▓▓▓▓] [░░░░] [░░░░]
                ↑ current
```

---

## Files Modified

**2 files changed:**

1. **templates/index.html**
   - `loadStories()` → Group stories by username
   - `viewUserStories()` → New function to load all user stories

2. **templates/base.html**
   - `openStoryViewerWithStories()` → New function to handle multiple stories

---

## Testing

### Test Case 1: Single Story User
1. User A posts 1 story
2. Home page shows [User A] once ✅
3. Click → Shows 1 story ✅

### Test Case 2: Multiple Stories User
1. User B posts 3 stories
2. Home page shows [User B] once (not 3 times) ✅
3. Click → Shows all 3 stories in sequence ✅
4. Progress bars show 3 bars ✅

### Test Case 3: Mixed Users
1. sam posts 2 stories
2. adam posts 3 stories
3. john posts 1 story
4. Home page shows: [sam] [adam] [john] ✅
5. Click sam → 2 stories ✅
6. Click adam → 3 stories ✅
7. Click john → 1 story ✅

### Test Case 4: Viewed State
1. User A posts 2 stories
2. View only 1st story
3. Circle still shows gradient (unviewed) ✅
4. View 2nd story
5. Circle turns grey (all viewed) ✅

---

## Summary

| Feature | Before | After |
|---------|--------|-------|
| Stories per user | Multiple circles | Single circle ✅ |
| UI clutter | High (7 items) | Low (3 items) ✅ |
| Story navigation | Single story only | All user stories ✅ |
| Progress bars | 1 bar only | Multiple bars ✅ |
| Instagram-like | ❌ No | ✅ Yes |
| Viewed state | Per story | Per user (smart) ✅ |

---

**Status:** ✅ **FIXED**  
**Behavior:** Instagram-like story grouping  
**Impact:** Cleaner UI, better UX  
**Date:** October 2, 2025

இப்போ sam ஒரு circle-ல 2 stories, adam ஒரு circle-ல 3 stories! 🎉
