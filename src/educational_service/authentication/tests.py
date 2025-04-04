from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


mock_user_create_data = [
    (
        {
             "username": "test",
             "email": "test@test.com",
             "password": "test123",
             "password2": "test123",
        },
        [status.HTTP_201_CREATED, {'message': 'User registered successfully'}]
    ),
    (
        {
             "username": "test",
             "email": "test@test.com",
             "password": "test123",
             "password2": "test123",
        },
        [status.HTTP_400_BAD_REQUEST, {'username': ['A user with that username already exists.']}]
    ),
    (
        {
             "username": "test1",
             "email": "test@test.com",
             "password": "test123",
             "password2": "test321",
        },
        [status.HTTP_400_BAD_REQUEST, {'detail': ["Password fields didn't match."]}]
    ),
    (
        {
             "username": "test2",
             "password": "test123",
             "password2": "test123",
        },
        [status.HTTP_400_BAD_REQUEST, {'detail': ["Field 'email' is required."]}]
    ),
    (
        {
             "username": "test3",
             "email": "test@test.com",
             "password": 1,
             "password2": "test123",
        },
        [status.HTTP_400_BAD_REQUEST, {'detail': ["Password fields didn't match."]}]
    ),
]

mock_authentication_data = [
    (
        {'username': 'test_username', 'password': 'test_password'},
        [status.HTTP_200_OK, None]
    ),
    (
        {'username': 'test_username1', 'password': 'test_password'},
        [status.HTTP_400_BAD_REQUEST, {'non_field_errors': ['Unable to log in with provided credentials.']}]
    ),
    (
        {'username': 'test_username',},
        [status.HTTP_400_BAD_REQUEST, {'password': ['This field is required.']}]
    ),
]

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_users_create(self):
        for data, (status_code, detail) in mock_user_create_data:
            response = self.client.post(path='/api/auth/register/', data=data)

            self.assertEqual(response.status_code, status_code)
            self.assertEqual(response.json(), detail)

    def test_authentication(self):
        User.objects.create_user(
            username="test_username",
            password="test_password",
            email="test_email@test.com"
        )
        for data, (status_code, detail) in mock_authentication_data:
            response = self.client.post(path='/api/auth/authenticate/', data=data)

            self.assertEqual(response.status_code, status_code)

            if status_code != status.HTTP_200_OK:
                self.assertEqual(response.json(), detail)