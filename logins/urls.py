from django.urls import path
from . import views

app_name='logins'

urlpatterns = [

    path('',views.landing_page,name='landing_page'),

    path('choose/',views.choose,name='choose'),

    path('index/', views.index, name='index'),

    path('signup_view/',views.signup_view,name='signup_view'),

    path('login_view/', views.login_view, name='login_view'),

    path('logout_view/', views.logout_view, name='logout_view'),

]
