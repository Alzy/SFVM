#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv
# LOAD ENVIRONMENT VARIABLES FROM .ENV IN THE PROJECTS ROOT FOLDER
project_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(project_dir, '.env')
load_dotenv(dotenv_path)

# update DATABASE_NAME to use \$ instead of $ else commands wont work
os.putenv(
    "DATABASE_NAME",
    str(os.getenv("DATABASE_NAME")).replace('$', '\\$')
)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sfvm.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
