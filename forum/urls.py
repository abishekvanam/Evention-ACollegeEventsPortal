from django.urls import path, re_path, include
from . import views

app_name='forum'

urlpatterns = [
    path('', views.begin, name='begin'),

    path('display_ques/', views.display_ques, name='display_ques'),

    path('<int:question_id>/', views.display_ans, name='display_ans'),

    path('ask/', views.ask, name='ask'),

    path('questions/', views.ask_questions, name='ask_questions'),

    path('ind/', views.indd, name='indd'),

    ]
