import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_rental_system.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin"
    )
    print("✅ Superuser created: admin / admin123")
else:
    print("ℹ️ Superuser already exists")