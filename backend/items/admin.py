from django.contrib import admin

from items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Item Admin
    """
    model = Item
    fields = (
        'name',
        'created_at'
    )
    readonly_fields = fields

    list_display = fields
