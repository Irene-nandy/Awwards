from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from AwardsUsers import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('update_profile', user_views.update_profile, name='update_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='AwardsUsers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='AwardsUsers/logout.html'), name='logout'),
]