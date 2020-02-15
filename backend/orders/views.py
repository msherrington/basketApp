from rest_framework import viewsets

from items.models import Item
from orders.models import Order
from orders.serializers import OrderSerializer
from orderitems.models import OrderItem


class OrderViewSet(viewsets.ModelViewSet):
    """ Order ViewSet """
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
            order_item.save()

            order.order_items.add(order_item)
        return Order.objects.filter(id=order.id)


def get_or_create_item(item_name):
    """
    Get or Create an Item instance

    :param item_name: string
    :return item: Item instance
    """
    try:
        item = Item.objects.get(name=item_name)
    except Item.DoesNotExist:
        item = Item()
        item.name = item_name
        item.save()
    return item
