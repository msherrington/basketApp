from django.db import models


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    item = models.ForeignKey(null=True, blank=True, on_delete=models.DO_NOTHING, to='items.Item')
    order = models.ForeignKey(null=True, blank=True, related_name='order_items',
                              on_delete=models.DO_NOTHING, to='orders.Order')

    def __str__(self):
        return '{} x {}'.format(self.quantity, self.item.name)

    def item_name(self):
        if self.item:
            return self.item.name
        return None
