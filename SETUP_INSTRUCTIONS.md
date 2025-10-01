# Instagram Clone - Setup Instructions

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### 1. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**On Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```bash
.\venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Test Data (IMPORTANT!)
This will create test users and posts so the Explore page works:
```bash
python run_test_data.py
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and navigate to:
- **Login Page:** http://127.0.0.1:8000/login
- **Home Page:** http://127.0.0.1:8000/

### Test Accounts
After running the test data script, you can log in with these accounts:

| Username | Password |
|----------|----------|
| john_doe | password123 |
| jane_smith | password123 |
| bob_wilson | password123 |
| alice_brown | password123 |
| charlie_davis | password123 |

## Troubleshooting

### "Failed to load posts" on Explore Page
This happens when there are no posts in the database. Run:
```bash
python run_test_data.py
```

### Permission Errors on Windows
If you get permission errors when activating the virtual environment:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Module Not Found Errors
Make sure you've activated the virtual environment and installed all dependencies:
```bash
pip install -r requirements.txt
```
