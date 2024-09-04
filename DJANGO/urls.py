
from django.contrib import admin
from django.urls import path
from resume.views import resume_view

urlpatterns = [
    path('', resume_view, name='ramki'),
   
]
