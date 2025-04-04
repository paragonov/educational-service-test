from django.urls import path, include
from . import auth, questions

urlpatterns = [
    path("auth/", include(auth.urlpatterns)),
    path("questions/", include(questions.urlpatterns)),
]
