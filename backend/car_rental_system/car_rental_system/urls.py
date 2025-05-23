"""
URL configuration for car_rental_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import CustomTokenObtainPairView
from users.views import RegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('users/', include('users.urls')),
        path('vehicles/', include('vehicles.urls')),
        path('bookings/', include('bookings.urls')),
        path('payments/', include('payments.urls')),
        path('reports/', include('reports.urls')),
        path('auth/', include([

            path('register/', RegisterView.as_view(), name='register'),
            path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        ])),
    ])),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
