from django.urls import path
from . import views

urlpatterns = [
    path('epic', views.PrimaryQueryView.as_view(), name='PrimaryQueryView'),
]