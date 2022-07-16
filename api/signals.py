from api.models import Order
from django.dispatch import receiver
from django.db.models.signals import pre_save


@receiver(pre_save, sender=Order)
def order_item_price(sender, instance, *args, **kwargs):
    """Updates order total price based on quantity before saving"""
    total = instance.product.price * instance.quantity
    instance.total_price = total

