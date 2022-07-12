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
        fields = ["name", "price", "description", "category", "category_name", "stock", "image"]


class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_product_name(self, obj):
        return obj.product.name

    def get_description(self, obj):
        return obj.product.description

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['status', 'date_created', 'total_price',
                            'product_name', 'description']


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
