from api.models import Product, Order
from django.contrib.auth.models import User
from rest_framework import generics, status, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.serializers import ProductSerializer, OrderSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly


class ProductList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.filter(user__id=self.request.user.id)
        return queryset


class OrderDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset.filter(user__id=self.request.user.id)
        return queryset


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(id=self.request.user.id)
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(id=self.request.user.id)
        return queryset