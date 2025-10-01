import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialapp.settings')
django.setup()

# Now import and run the test data creation
exec(open('create_test_data.py').read())
