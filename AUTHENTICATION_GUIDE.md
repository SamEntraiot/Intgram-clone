# Instagram Clone - Authentication Guide

## 🔐 Authentication Features

This Instagram clone includes a complete authentication system with the following features:

### ✅ Implemented Features

1. **User Registration**
   - Manual signup with email, username, and password
   - Client-side and server-side validation
   - Password strength requirements (minimum 8 characters)
   - Username uniqueness validation
   - Email format validation

2. **Google OAuth Login**
   - One-click Google sign-in
   - Automatic account creation for new Google users
   - Username generation from Google profile data
   - Seamless JWT token integration

3. **User Login/Logout**
   - Login with username or email
   - JWT token-based authentication
   - Secure logout functionality
   - Session management

4. **Profile Creation**
   - Automatic profile creation on user registration
   - Profile picture upload support
   - Bio and website fields
   - User statistics (posts, followers, following)

5. **Password Reset**
   - Email-based password reset
   - Secure token generation
   - Password reset confirmation page
   - Link expiration handling

## 🚀 Getting Started

### 1. Setup Environment

```bash
# Copy environment file
cp .env.example .env

# Edit .env with your Google OAuth credentials
# Get credentials from: https://console.cloud.google.com/
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

```bash
python manage.py migrate
```

### 4. Run the Server

```bash
python manage.py runserver
```

## 🔧 Configuration

### Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google+ API and Google OAuth2 API
4. Go to Credentials > Create Credentials > OAuth 2.0 Client IDs
5. Set Application type to "Web application"
6. Add authorized redirect URIs:
   - `http://localhost:8000/accounts/google/login/callback/`
   - `http://127.0.0.1:8000/accounts/google/login/callback/`
7. Copy the Client ID and Client Secret to your `.env` file

### Email Configuration (Optional)

For password reset functionality, configure email settings in `.env`:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 📱 User Interface

### Authentication Pages

- **Login Page**: `/login`
  - Username/email and password login
  - Google OAuth button
  - Forgot password link
  - Link to registration page

- **Registration Page**: `/register`
  - Manual signup form
  - Google OAuth option
  - Form validation
  - Terms and conditions

- **Password Reset**: `/reset-password/<uid>/<token>/`
  - Secure password reset form
  - Token validation
  - New password confirmation

### Navigation Features

- **Logout Button**: Available in the main navigation sidebar
- **Profile Access**: Direct access to user profile
- **Authentication State**: Automatic redirection based on login status

## 🔒 Security Features

### Password Security
- Minimum 8 character requirement
- Password confirmation validation
- Secure password hashing using Django's built-in system

### Token Security
- JWT tokens for API authentication
- Refresh token rotation
- Secure token storage in localStorage

### OAuth Security
- Secure Google OAuth integration
- Automatic username generation
- Email verification through Google

### Form Validation
- Client-side validation for immediate feedback
- Server-side validation for security
- CSRF protection on all forms

## 🛠 API Endpoints

### Authentication Endpoints

```
POST /api/register/          - User registration
POST /api/login/             - User login (JWT)
POST /api/token/refresh/     - Refresh JWT token
GET  /api/auth/get-jwt-token/ - Get JWT for OAuth users
```

### Password Reset Endpoints

```
POST /api/password-reset/         - Request password reset
POST /api/password-reset-confirm/ - Confirm password reset
```

### Profile Endpoints

```
GET  /api/profile/me/              - Get current user profile
PUT  /api/profile/me/              - Update current user profile
GET  /api/profile/<username>/      - Get user profile by username
```

## 🎨 UI/UX Features

### Responsive Design
- Mobile-first approach
- Tablet and desktop optimizations
- Touch-friendly interface

### User Experience
- Loading states and feedback
- Error message handling
- Success confirmations
- Smooth transitions

### Instagram-like Styling
- Authentic Instagram color scheme
- Modern typography
- Clean, minimal design
- Consistent spacing and layout

## 🧪 Testing

### Manual Testing Checklist

- [ ] User can register with email/username/password
- [ ] User can login with Google OAuth
- [ ] User can login with username/email and password
- [ ] User can logout successfully
- [ ] User can reset password via email
- [ ] Profile is created automatically on registration
- [ ] Form validation works correctly
- [ ] Authentication state is maintained across pages
- [ ] Responsive design works on all devices

### Test User Accounts

After running migrations, you can create test accounts:

```bash
python manage.py createsuperuser
```

## 🔄 Future Enhancements

Potential improvements for the authentication system:

- [ ] Two-factor authentication (2FA)
- [ ] Social login with Facebook, Twitter
- [ ] Account verification via email
- [ ] Password strength indicator
- [ ] Login attempt rate limiting
- [ ] Account lockout after failed attempts
- [ ] Remember me functionality
- [ ] Single Sign-On (SSO) integration

## 🐛 Troubleshooting

### Common Issues

1. **Google OAuth not working**
   - Check if Google+ API is enabled
   - Verify redirect URIs are correct
   - Ensure .env file has correct credentials

2. **Password reset emails not sending**
   - Check email configuration in settings.py
   - Verify EMAIL_BACKEND is set correctly
   - For development, check console output

3. **JWT tokens not working**
   - Clear localStorage and try again
   - Check if tokens are expired
   - Verify API endpoints are accessible

4. **Registration validation errors**
   - Check password meets minimum requirements
   - Ensure username is unique
   - Verify email format is correct

## 📞 Support

If you encounter any issues with the authentication system, please check:

1. Server logs for detailed error messages
2. Browser console for JavaScript errors
3. Network tab for API request/response details
4. Database for user account status

---

**Note**: This authentication system is designed for development and demonstration purposes. For production use, consider additional security measures such as rate limiting, HTTPS enforcement, and comprehensive logging.
