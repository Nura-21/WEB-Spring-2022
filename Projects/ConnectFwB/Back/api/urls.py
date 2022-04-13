from django.urls import path, include
from rest_framework import routers
 
from . import views
 
 
urlpatterns = [
    path('users/', views.UserViewSet.as_view()),
     path('users/<int:pk>/', views.UserDetailAPIView.as_view()),
]