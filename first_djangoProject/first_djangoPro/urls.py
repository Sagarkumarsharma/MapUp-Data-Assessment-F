"""first_djangoPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from users_app import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name = 'register-app'), #add the path of users_app views for register
    path('profile/', users_views.profile, name = 'profile-app'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users_app/login.html'), name = 'login-app'), #add views of login 
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users_app/logout.html'), name = 'logout-app'), #add views of logout
    path('', include('django_app.urls')), #here we have included django_app.urls path as a string
    
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 