from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import response, status, permissions

from authentication.serializers import RegistrationSerializer, LoginSerializer

from api.permissions import IsNotAuthenticatedOrReadOnly
from rest_framework import generics

from authentication.models import User


class UserListAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegistrationSerializer(user)
        return response.Response({'user': serializer.data})


class RegistrationAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(
            {'message': "Invalid credentials, try again"},
            status=status.HTTP_401_UNAUTHORIZED
        )
