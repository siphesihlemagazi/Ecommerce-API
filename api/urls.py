from django.urls import path
from api.views import ProductList, ProductDetail

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<str:pk>', ProductDetail.as_view()),
]
