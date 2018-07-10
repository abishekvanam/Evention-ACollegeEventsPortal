from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.view_profile, name='view_profile'),
    path('accounts/login/events/', views.events_redirect, name='events_redirect'),
    path('accounts/signup/events/', views.signup_redirect, name='signup_redirect'), #
]
