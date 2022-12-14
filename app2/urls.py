from django.contrib import admin
from django.urls import path
from app2.views import *
app_name='inner'
urlpatterns = [
path('page/',page,name='page')
]