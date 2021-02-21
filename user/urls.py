from django.urls import path
from .views import UserCreate, UserLogin


urlpatterns = [
    path('/signup', UserCreate.as_view(), name='signup'),
    path('/signin', UserLogin.as_view(), name='signin'),
]

