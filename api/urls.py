from django.urls import path
from api.views import ProductList, ProductDetail, OrderList, OrderDetail, UserList, UserDetail

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<str:pk>', ProductDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<str:pk>', OrderDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<str:pk>', UserDetail.as_view()),
]
