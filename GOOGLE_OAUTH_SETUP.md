# Google OAuth Setup Guide

## Prerequisites
1. A Google account
2. Access to Google Cloud Console

## Step-by-Step Setup

### 1. Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "New Project"
3. Enter project name (e.g., "Instagram Clone")
4. Click "Create"

### 2. Enable Google+ API
1. In the Google Cloud Console, go to "APIs & Services" → "Library"
2. Search for "Google+ API" 
3. Click on it and press "Enable"

### 3. Create OAuth 2.0 Credentials
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth 2.0 Client IDs"
3. If prompted, configure the OAuth consent screen:
   - Choose "External" user type
   - Fill in required fields (App name, User support email, Developer contact)
   - Add your domain or use localhost for development
   - Save and continue through all steps

### 4. Configure OAuth Client
1. Select "Web application" as application type
2. Add authorized redirect URIs:
   ```
   http://localhost:8000/accounts/google/login/callback/
   http://127.0.0.1:8000/accounts/google/login/callback/
   ```
3. Click "Create"
4. Copy the Client ID and Client Secret

### 5. Configure Environment Variables
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` file and add your credentials:
   ```
   GOOGLE_CLIENT_ID=your_actual_client_id_here
   GOOGLE_CLIENT_SECRET=your_actual_client_secret_here
   ```

### 6. Run Migrations and Start Server
```bash
python manage.py migrate
python manage.py runserver
```

### 7. Test Google OAuth
1. Go to http://localhost:8000/login
2. Click "Log in with Google"
3. Complete the Google authentication flow
4. You should be redirected back to the app and logged in

## Troubleshooting

### Common Issues:
1. **"redirect_uri_mismatch" error**: Make sure the redirect URI in Google Console exactly matches the one being used
2. **"invalid_client" error**: Check that your Client ID and Secret are correct in the .env file
3. **"access_denied" error**: Make sure your OAuth consent screen is properly configured

### Development vs Production:
- For development: Use `localhost:8000` and `127.0.0.1:8000`
- For production: Add your actual domain to authorized redirect URIs

## Security Notes:
- Never commit your `.env` file to version control
- Keep your Client Secret secure
- Use HTTPS in production
- Regularly rotate your OAuth credentials
