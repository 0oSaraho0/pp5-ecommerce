from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem())
def update_on_save(sender, instance, created, **kwarks):
    """ Update order total lineitem update/create """

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem())
def delete_on_save(sender, instance, **kwarks):
    """ Update order total lineitem delete """

    instance.order.update_total()