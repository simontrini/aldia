"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

import sys

from django.core.wsgi import get_wsgi_application

# Añade esta parte ANTES de la configuración de Django
path = '/home/aldia/mysite'  # Ruta ABSOLUTA a tu proyecto
if path not in sys.path:
    sys.path.insert(0, path)
    #print(sys.path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
