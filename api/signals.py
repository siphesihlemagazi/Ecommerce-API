from django.db.models.signals import pre_save
from django.dispatch import receiver

from api.models import Order


def pre_save_order_tem_receiver(sender, instance, *args, **kwargs):

    """Updates order total price based on quantity before saving"""

    total = instance.product.price * instance.quantity
    instance.total_price = total


pre_save.connect(pre_save_order_tem_receiver, sender=Order)
