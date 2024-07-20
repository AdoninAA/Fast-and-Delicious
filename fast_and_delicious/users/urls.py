from django.urls import path
from .views import UserRegisterView, UserLoginView, UserProfileUpdateView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileUpdateView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
