from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.core import views  # Import the register view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Define una vista específica para la raíz
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('productos/', views.productos, name='productos'),
    path('servicios/', views.servicios, name='servicios'),
]

