from rest_framework import viewsets

from items.services.item_service import get_or_create_item
from orders.models import Order
from orders.serializer import OrderSerializer
from orderitems.models import OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    """
    Order ViewSet
    """

    serializer_class = OrderSerializer

    def get_queryset(self):
        order_items = self.request.data.get('order_items', None)

        order = Order()
        order.save()

        for item in order_items:
            item_name = item['item_name']
            quantity = item['quantity']

            new_item = get_or_create_item(item_name)

            order_item = OrderItem()
            order_item.item = new_item
            order_item.quantity = quantity
            order_item.order = order
            order_item.save()

        return Order.objects.filter(id=order.id)
