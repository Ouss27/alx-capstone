from django.urls import path
from .views import UserRegistrationView, UserDetailView, UserDeleteView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'), # user registration
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-profile'), # user view/update his info
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'), # delete user (Only admin users can delete users)
    path('login/', obtain_auth_token, name='api-login'),  # Login endpoint
    path('logout/', LogoutView.as_view(), name='api-logout'),  # Logout endpoint
]
