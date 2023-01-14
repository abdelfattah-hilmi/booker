from django.urls import path 
from .views import UserRegister


urlpatterns = [
    path('register/', UserRegister.as_view(), name = 'User_registration_endpoint' ),
]