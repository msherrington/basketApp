from rest_framework import serializers

from orderitems.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """
    OrderItem Serializer.
    """

    class Meta:
        model = OrderItem

        fields = (
            'quantity',
            'item_name'
        )
        read_only_fields = fields
