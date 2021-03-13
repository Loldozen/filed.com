from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

#app_name = 'audios'

urlpatterns = [
    path('', views.api_root),
    path('create/', views.CreateAPI.as_view(), name='create-file'),
    path('list/', views.ListFiles.as_view(), name='list-files'),
    path('read/<int:pk>/', views.FileDetails.as_view(), name='read-file'),
    path('update/<int:pk>/', views.UpdateFile.as_view(), name='update-file'),
    path('delete/<int:pk>/', views.DeleteFile.as_view(), name='delete-file'),
]

urlpatterns = format_suffix_patterns(urlpatterns)