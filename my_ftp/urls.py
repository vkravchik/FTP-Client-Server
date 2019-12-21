from django.urls import path
from . import views
urlpatterns = [
    path('connect', views.connect, name='connect'),
    path('get_dir', views.get_dir_content, name='get_dir_content'),
    path('download_file', views.download_file, name='download_file')
]