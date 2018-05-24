"""
WSGI config for sfvm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

# LOAD ENVIRONMENT VARIABLES FROM .ENV IN THE PROJECTS ROOT FOLDER
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(project_dir, '.env')
load_dotenv(dotenv_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sfvm.settings")

application = get_wsgi_application()
