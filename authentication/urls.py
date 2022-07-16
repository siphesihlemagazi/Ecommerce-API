from django.urls import path
from authentication.views import RegistrationAPIView, LoginAPIView, UserListAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
]
