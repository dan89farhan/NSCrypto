"""
WSGI config for cryptoserver project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cryptoserver.settings")

application = get_wsgi_application()

# please remove the below comment to run on local server


# from whitenoise.django import DjangoWhiteNoise
# application = DjangoWhiteNoise(application)