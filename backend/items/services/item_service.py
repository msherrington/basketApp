from items.models import Item


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
