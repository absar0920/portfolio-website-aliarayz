from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('videos/', views.all_videos, name='all_videos'),
    path('projects/', views.all_projects, name='all_projects'),
]
