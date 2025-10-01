# Testing the Suggestions Feature

## Quick Test Steps

### 1. Start the Server
```bash
python manage.py runserver
```

### 2. Open Browser
Navigate to: `http://localhost:8000`

### 3. Test the Feature

#### Test Case 1: View Suggestions
1. Log in with your account
2. Go to the home page
3. Look at the right sidebar
4. You should see "Suggestions For You" section with user suggestions

#### Test Case 2: Follow a Suggested User
1. Click the "Follow" button on any suggested user
2. The button should change to "Following"
3. The suggestion should fade out and disappear after 1 second

#### Test Case 3: Check Suggestion Logic
1. Log in as User A
2. Follow some users (User B, User C)
3. Log out and log in as User B
4. Follow User D
5. Log out and log back in as User A
6. Check suggestions - User D should appear (friend of friend)

#### Test Case 4: No Suggestions Available
1. Create a new user account
2. If there are no other users, you'll see "No suggestions available"

## API Testing

### Using Browser Console

Open browser console (F12) and run:

```javascript
// Test the suggestions endpoint
fetch('/api/suggestions/', {
    headers: {
        'Authorization': `Bearer ${localStorage.getItem('authToken')}`
    }
})
.then(r => r.json())
.then(data => console.log('Suggestions:', data));
```

Expected response:
```json
[
    {
        "id": 2,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "profile": {
            "avatar": "/media/avatars/test.jpg",
            "bio": "Test bio"
        },
        "is_following": false
    }
]
```

### Using curl (Command Line)

```bash
# Get auth token first
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"your_username","password":"your_password"}'

# Use the access token to get suggestions
curl http://localhost:8000/api/suggestions/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Using Postman or Thunder Client

1. **Login Request**:
   - Method: POST
   - URL: `http://localhost:8000/api/login/`
   - Body: `{"username": "your_user", "password": "your_pass"}`
   - Save the `access` token

2. **Get Suggestions**:
   - Method: GET
   - URL: `http://localhost:8000/api/suggestions/`
   - Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN`

## Edge Cases to Test

### Empty Database
- **Scenario**: No other users exist
- **Expected**: Returns empty array or shows "No suggestions available"

### User Follows Everyone
- **Scenario**: User already follows all available users
- **Expected**: Returns empty array

### New User with No Followers
- **Scenario**: Brand new user, nobody follows them
- **Expected**: Returns random users from the database

### Only Following One Person
- **Scenario**: User follows only one person
- **Expected**: Returns users followed by that person + random users

## Expected Behaviors

### ✅ Success Indicators
- Suggestions load within 2 seconds
- Shows 1-5 suggested users
- "Follow" button works correctly
- After following, suggestion fades out
- No duplicate suggestions
- Current user not in suggestions
- Already followed users not in suggestions

### ❌ Error Indicators to Fix
- Suggestions container shows "Loading..." forever
- Console errors about 404 or 403
- Follow button doesn't work
- Suggestions include current user
- Suggestions include already followed users

## Debugging

### Check Browser Console
Look for errors like:
- `Failed to load suggestions`
- `HTTP error! status: 404` - Endpoint not found
- `HTTP error! status: 401` - Not authenticated
- `HTTP error! status: 500` - Server error

### Check Django Console
Look for:
- Python errors or tracebacks
- Database query errors
- Missing Profile errors

### Common Issues

**Issue**: 404 Error on `/api/suggestions/`
- **Fix**: Verify URL is added to `accounts/urls.py`

**Issue**: 500 Server Error
- **Fix**: Check Django console for traceback
- Ensure Profile model is properly set up
- Check that post_save signals are working

**Issue**: No suggestions showing
- **Fix**: Ensure other users exist in database
- Run `python create_test_data.py` to generate test users

**Issue**: "Loading..." never changes
- **Fix**: Check browser console for JavaScript errors
- Verify authToken exists in localStorage
- Check API response in Network tab

## Performance Testing

For large databases:
```python
# In Django shell (python manage.py shell)
from django.contrib.auth.models import User
from accounts.models import Profile
import time

# Test suggestion query performance
start = time.time()
user = User.objects.first()
# Simulate the suggestion logic
from accounts.views import get_suggestions
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request

factory = APIRequestFactory()
request = factory.get('/api/suggestions/')
request.user = user
response = get_suggestions(request)
end = time.time()

print(f"Query time: {end - start} seconds")
print(f"Suggestions count: {len(response.data)}")
```

Expected query time: < 1 second for databases with < 10,000 users
