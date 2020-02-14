from django.db import models

from orders.services.order_number_service import generate_order_number


class Order(models.Model):
    order_number = models.PositiveIntegerField(unique=True, default=generate_order_number)
    order_items = models.ForeignKey(null=True, blank=True, on_delete=models.CASCADE, to='orderitems.OrderItem')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Order submitted at {}'.format(self.submitted_at)
