from rest_framework import serializers

from orders.models import Order
from orderitems.serializer import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    """
    Order Serializer
    """

    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'order_number',
            'order_items'
        )
        read_only_fields = fields
