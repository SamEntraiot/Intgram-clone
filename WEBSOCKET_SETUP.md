# WebSocket Real-Time Messaging Setup

## Overview
This Instagram clone now uses WebSocket protocol for real-time messaging, replacing the previous polling mechanism.

## Installation Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

The following packages have been added:
- `channels>=4.0.0` - Django Channels for WebSocket support
- `channels-redis>=4.1.0` - Redis channel layer (optional, for production)
- `daphne>=4.0.0` - ASGI server

### 2. Run the Development Server

**Important:** Use Daphne instead of the default Django development server:

```bash
daphne -p 8000 socialapp.asgi:application
```

Or for binding to all interfaces:
```bash
daphne -b 0.0.0.0 -p 8000 socialapp.asgi:application
```

### 3. Alternative: Run with Django Command (Development Only)
```bash
python manage.py runserver
```
Note: Django's runserver will automatically use Daphne when `daphne` is in INSTALLED_APPS.

## Features

### ✅ Real-Time Messaging
- Messages are delivered instantly via WebSocket
- No more 3-second polling delay
- Reduced server load

### ✅ Typing Indicators
- See when other users are typing
- Automatically disappears after 3 seconds of inactivity

### ✅ Automatic Reconnection
- WebSocket automatically reconnects if connection is lost
- Seamless fallback to REST API if WebSocket fails

### ✅ Message Deduplication
- Messages are tagged with unique IDs
- Prevents duplicate messages from appearing

### ✅ Smart Scrolling
- Auto-scrolls only if user is at bottom
- Preserves scroll position when viewing older messages

## Architecture

### Backend Components

1. **Consumer** (`accounts/consumers.py`)
   - Handles WebSocket connections
   - Manages chat rooms using channel layers
   - Authenticates users and validates participants

2. **Routing** (`accounts/routing.py`)
   - Maps WebSocket URLs to consumers
   - URL pattern: `ws://localhost:8000/ws/chat/<conversation_id>/`

3. **ASGI** (`socialapp/asgi.py`)
   - Configures ASGI application
   - Routes HTTP and WebSocket protocols

### Frontend Components

1. **WebSocket Connection**
   - Establishes connection when opening a conversation
   - Handles reconnection on failure

2. **Message Handling**
   - Sends messages via WebSocket
   - Falls back to REST API if WebSocket unavailable

3. **Typing Indicators**
   - Broadcasts typing status to other participants
   - Debounced to avoid excessive updates

## Production Deployment

### Redis Channel Layer (Recommended)

For production, use Redis instead of InMemoryChannelLayer:

1. Install Redis:
```bash
pip install channels-redis
```

2. Update `settings.py`:
```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

3. Start Redis server:
```bash
redis-server
```

### ASGI Server

Use Daphne or Uvicorn for production:

**With Daphne:**
```bash
daphne -u /tmp/daphne.sock socialapp.asgi:application
```

**With Uvicorn:**
```bash
pip install uvicorn
uvicorn socialapp.asgi:application --host 0.0.0.0 --port 8000
```

### Nginx Configuration

```nginx
upstream django {
    server unix:/tmp/daphne.sock;
}

server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://django;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Troubleshooting

### WebSocket Connection Fails

1. Check console for errors (F12)
2. Verify server is running with Daphne
3. Check URL pattern matches: `ws://localhost:8000/ws/chat/<id>/`

### Messages Not Appearing

1. Check WebSocket connection status in console
2. Verify user is authenticated
3. Check user is participant in conversation

### Typing Indicator Not Working

1. Ensure WebSocket is connected
2. Check browser console for errors
3. Verify handleInputChange is attached to input

## Testing

1. Open two browser windows (or one incognito)
2. Log in as different users
3. Start a conversation
4. Send messages - they should appear instantly
5. Type in one window - typing indicator appears in other

## Fallback Behavior

If WebSocket fails:
- Messages fallback to REST API
- Polling can be re-enabled
- User experience degrades gracefully

## Future Enhancements

- [ ] Read receipts
- [ ] Message reactions
- [ ] File/image sharing via WebSocket
- [ ] Voice messages
- [ ] Video calls
- [ ] Group chat support
- [ ] Message encryption
