from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f"{self.name}".title()


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=1)
    image = ResizedImageField(default='placeholder.png', size=[300, 300],
                              crop=['middle', 'center'], quality=75,
                              force_format="PNG",
                              upload_to='products')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f"{self.name} ({self.category}) R{self.price}".title()


class Order(models.Model):
    statuses = [('Delivered', 'Delivered'), ('Pending', 'Pending')]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=statuses, default='Pending')
    date_created = models.DateTimeField(default=datetime.now)
    total_price = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.product.name} x{self.quantity} - {self.total_price}".title()

