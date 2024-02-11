# itemDashboard/urls.py

from django.urls import path
from .views import ItemListAPIView
from django.contrib.auth import views as auth_views
from . import views
from itemDashboard.views import UserRegistrationAPIView, UserLoginAPIView
from itemDashboard.views import ItemCreateAPIView

urlpatterns = [
    path('items/', ItemListAPIView.as_view(), name='item-list'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('register/',UserRegistrationAPIView.as_view(), name='user-register'),
    path('items/create/', ItemCreateAPIView.as_view(), name='create-item') 
]
