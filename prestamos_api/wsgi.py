"""
WSGI config for prestamos_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prestamos_api.settings')

application = get_wsgi_application()


# prestamos_api/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prestamos_api.settings')

application = get_wsgi_application()

# Llamar a creación del superusuario si aplica
try:
    from .create_superuser import create_admin
    create_admin()
except Exception as e:
    print(f"Error creando superusuario: {e}")
