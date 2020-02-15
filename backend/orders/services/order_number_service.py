def generate_order_number():
    from orders.models import Order
    if Order.objects.count() > 0:
        return Order.objects.order_by('id').last().order_number + 1
    return 1000
