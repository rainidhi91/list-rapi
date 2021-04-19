"""
WSGI config for p_list_rapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

load_dotenv()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'p_list_rapi.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get("MY_PROJECT_SETTING", "p_list_rapi.settings.development"))


application = get_wsgi_application()
