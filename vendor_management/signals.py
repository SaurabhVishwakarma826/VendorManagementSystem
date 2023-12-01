# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder

@receiver(post_save, sender=PurchaseOrder)
def purchase_order_post_save(sender, instance, **kwargs):
    from .performance import calculate_performance_history
    calculate_performance_history(instance.vendor)
