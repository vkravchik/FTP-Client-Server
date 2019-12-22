from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from connection import views

urlpatterns = [
    path('', views.get_or_post),
    path('/<int:pk>', views.get_or_put_or_delete, name="get or put"),
]