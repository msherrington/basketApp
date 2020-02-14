from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Order Admin
    """
    model = Order
    fields = (
        'order_number',
        'items',
        'submitted_at'
    )
    readonly_fields = fields

    list_display = fields
