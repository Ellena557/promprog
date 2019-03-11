from django.urls import path 
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.all_questions, name='all_questions'),
    path('new/', views.new_question, name='new_question'),
    path('<int:pk>/', views.question, name='question'),
]
