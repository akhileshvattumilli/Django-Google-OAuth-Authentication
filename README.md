# Django Google OAuth Authentication

A Django authentication module implementing Google OAuth 2.0 with PKCE (Proof Key for Code Exchange) security enhancements. This project provides a robust authentication system that can be easily integrated into your existing Django applications, featuring secure token handling, state validation, and user session management.

## Features

- **Google OAuth 2.0 Integration**: Secure authentication using Google accounts
- **PKCE Security**: Implements Proof Key for Code Exchange for enhanced security
- **State Validation**: Prevents CSRF attacks with secure state parameter handling
- **Session Management**: Django-based user session handling and authentication
- **Secure Token Handling**: JWT token verification and validation
- **CSRF Protection**: Built-in Django CSRF protection for all forms
- **User Management**: Automatic user creation and login from Google accounts
- **Easy Integration**: Simple to add to existing Django projects
- **Modular Design**: Self-contained authentication app that doesn't interfere with your existing code

## Technology Stack

- **Backend Framework**: Django 5.2.5
- **Authentication**: Google OAuth 2.0 with PKCE
- **Database**: SQLite3 (configurable for production)
- **Security**: Django security middleware, CSRF protection
- **Dependencies**: 
  - google-auth
  - google-auth-oauthlib
  - google-auth-httplib2
  - python-decouple
  - requests

## Prerequisites

- Python 3.8 or higher
- Google Cloud Platform account with OAuth 2.0 credentials
- Virtual environment (recommended)

## Installation

### Option 1: Standalone Application
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-google-oauth-auth
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .sample.env .env
   ```
   
   Edit `.env` file with your Google OAuth credentials:
   ```
   BASE_URL=http://127.0.0.1:8000
   GOOGLE_CLIENT_ID=your_google_client_id.apps.googleusercontent.com
   GOOGLE_SECRET_KEY=your_google_secret_key
   ```

5. **Run database migrations**
   ```bash
   cd src
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

### Option 2: Integrate into Existing Django Project
1. **Copy the `googler` app** to your Django project
2. **Add to INSTALLED_APPS** in your settings.py:
   ```python
   INSTALLED_APPS = [
       # ... your existing apps
       'googler',
   ]
   ```
3. **Include the URLs** in your main urls.py:
   ```python
   urlpatterns = [
       # ... your existing URLs
       path('google/', include('googler.urls')),
   ]
   ```
4. **Add required settings** to your settings.py:
   ```python
   GOOGLE_CLIENT_ID = 'your_client_id'
   GOOGLE_SECRET_KEY = 'your_secret_key'
   BASE_URL = 'http://yourdomain.com'
   LOGIN_REDIRECT_URL = '/dashboard/'  # Where to redirect after login
   ```
5. **Install required packages**:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 python-decouple requests
   ```

## Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google+ API
4. Go to Credentials → Create Credentials → OAuth 2.0 Client IDs
5. Set application type to "Web application"
6. Add authorized redirect URIs:
   - `http://127.0.0.1:8000/google/callback/` (development)
   - `https://yourdomain.com/google/callback/` (production)
7. Copy Client ID and Client Secret to your `.env` file

## Usage

### Standalone Application
1. Navigate to `http://127.0.0.1:8000/google/login/`
2. Click "Login with Google" button
3. Complete Google OAuth flow
4. User will be automatically logged in and redirected

### Integrated into Your Django App
1. Add login links to your templates:
   ```html
   <a href="{% url 'googler:login' %}">Login with Google</a>
   ```
2. Users can authenticate through Google OAuth
3. After successful authentication, they'll be redirected to your `LOGIN_REDIRECT_URL`
4. Access the authenticated user with `request.user` in your views

## Project Structure

```
src/
├── myproject/          # Django project settings (example project)
│   ├── settings.py     # Project configuration
│   ├── urls.py         # Main URL routing
│   └── wsgi.py         # WSGI application
├── googler/            # Google OAuth application (main module)
│   ├── oauth.py        # OAuth implementation
│   ├── views.py        # View handlers
│   ├── services.py     # Business logic
│   ├── security.py     # Security utilities
│   ├── models.py       # Data models
│   └── templates/      # HTML templates
├── manage.py           # Django management script
└── db.sqlite3          # SQLite database
```

**Note**: The `googler/` directory contains the main authentication module that you can copy into your existing Django projects.

## Security Features

- **PKCE Implementation**: Prevents authorization code interception attacks
- **State Parameter**: CSRF protection for OAuth flow
- **Token Validation**: JWT token verification with Google's public keys
- **Secure Headers**: Django security middleware enabled
- **HTTPS Support**: Configurable for production environments

## Configuration

### Environment Variables

- `BASE_URL`: Your application's base URL
- `GOOGLE_CLIENT_ID`: Google OAuth client ID
- `GOOGLE_SECRET_KEY`: Google OAuth client secret

### Django Settings

Key settings in `myproject/settings.py`:
- `GOOGLE_AUTH_CALLBACK_PATH`: OAuth callback path
- `LOGIN_REDIRECT_URL`: Redirect URL after successful login
- `ALLOWED_HOSTS`: Configure for production deployment

## Development

### Running Tests
```bash
cd src
python manage.py test
```

### Database Management
```bash
cd src
python manage.py makemigrations
python manage.py migrate
```

### Creating Superuser
```bash
cd src
python manage.py createsuperuser
```

## Production Deployment

1. Set `DEBUG = False` in settings
2. Configure production database (PostgreSQL recommended)
3. Set `ALLOWED_HOSTS` to your domain
4. Use HTTPS in production
5. Set secure `SECRET_KEY`
6. Configure static file serving
7. Use production WSGI server (Gunicorn, uWSGI)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
1. Check existing issues in the repository
2. Create a new issue with detailed description
3. Include error logs and environment details

## Acknowledgments

- Django framework and community
- Google OAuth 2.0 implementation
- Security best practices from OAuth 2.0 specification
# Django-Google-OAuth-Authentication
