from django.db import models


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    item = models.ForeignKey(null=True, blank=True, on_delete=models.DO_NOTHING, to='items.Item')

    def __str__(self):
        return '{} x {}'.format(self.quantity, self.item.name)

    def item_name(self):
        return self.item.name
