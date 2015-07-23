"""
WSGI config for medstart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'start.settings'

# os.environ.setdefault("DJANGO_SETTINGS_MODULE" = "start.settings")

application = get_wsgi_application()
