from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from educational_service.authentication.views import UserRegistrationView

urlpatterns = [
    path('authenticate/', obtain_auth_token, name='authentication'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]