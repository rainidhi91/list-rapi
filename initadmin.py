import os
os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv("MY_PROJECT_SETTING")
import django
django.setup()

from django.contrib.auth.management.commands.createsuperuser import get_user_model
if get_user_model().objects.filter(email='admin@pullstream.com').exists(): 
    print("Super user already created")
    print("UserList:")
    print(get_user_model().objects.filter(email='admin@pullstream.com'))
else:
    get_user_model()._default_manager.db_manager('default').create_superuser(email='admin@pullstream.com', password='adminPullStr3@m')
    print("Super user created successfully")