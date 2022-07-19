from rest_framework import serializers
from api.models import Category, Product, Order
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Product
        fields = ["id", "name", "price", "description", "category",
                  "category_name", "stock", "image"]


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    product_name = serializers.ReadOnlyField(source="product.name")
    description = serializers.ReadOnlyField(source="product.description")

    def get_customer(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['customer', 'status', 'created_at', 'updated_at',
                            'total_price', 'product_name', 'description', 'user']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
