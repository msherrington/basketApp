from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_number', 'order_items', 'submitted_at')
        read_only_fields = fields
