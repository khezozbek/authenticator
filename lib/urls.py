from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from .api import PasswordAPIView, PasswordUpdateAPIVIew, UserRegistrationView, redirect_to_login
from .views import Profile, login, register, CreatePassword, Detail
from django.contrib.auth.decorators import login_required  # Import login_required

router = SimpleRouter()

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),

    # profile
    path('', Profile, name='profile'),
    path('create/', CreatePassword, name="create"),
    path('detail/<int:pk>', Detail, name="detail"),

    # register api
    path('api/password/', PasswordAPIView.as_view(), name='password-list-create'),
    path('api/password/update-delete/', PasswordUpdateAPIVIew.as_view()),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', obtain_auth_token, name='login'),
    path('api/secure-endpoint/', login_required(redirect_to_login), name='secure-endpoint'),
]
