from django.contrib.auth import get_user_model
from django.core.management import execute_from_command_line
import os

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")

if not User.objects.filter(username=username).exists():
    print("Creando superusuario...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("Superusuario ya existe.")
