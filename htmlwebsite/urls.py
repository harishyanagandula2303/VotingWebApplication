from django.contrib import admin
from django.urls import path
from htmlwebsite import views
from .views import RegisterEndUserView

app_name = 'htmlwebsite'

urlpatterns = [
    path('', views.home, name='home'),
    path('endusers/', views.endusers_view, name='endusers'),
    path('register/', views.register_user, name='register'),
    path('enduser-registration/', views.enduser_registration, name='enduser_registration'),
    # other URL patterns for your app
    path('user_info/', views.user_info, name='user_info'),

    path('htmlwebsite/login/', views.Login, name='login'),
    path('register/', RegisterEndUserView.as_view(), name='register_enduser'),
    path('htmlwebsite/index3/', views.AfterLogin, name='index'),
    path('conduct-poll/', views.conduct_poll, name='conduct_poll'),
]