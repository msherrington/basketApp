from django.contrib import admin

from orderitems.models import OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    OrderItem Admin
    """
    model = OrderItem
    fields = (
        'item',
        'quantity',
    )
    readonly_fields = fields

    list_display = fields
