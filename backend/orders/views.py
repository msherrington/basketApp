from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view

from items.models import Item
from orders.models import Order
from orders.serializers import OrderSerializer
from django.http import HttpResponse
from django.views.generic import View
from orderitems.models import OrderItem
from django.views.decorators.csrf import csrf_exempt

import json


# @csrf_exempt
class OrderViewSet(viewsets.ModelViewSet):
    """Order ViewSet"""
    serializer_class = OrderSerializer

    def get_queryset(self):
        print('HHHHHHHHHHHHHHHHHHHHH', self.request.data)
        order_items = self.request.data.get('order_items', None)
        print('**************', order_items)
        # quantity = self.request.data.get('quantity', None)

        order = Order()
        order.save()

        for item in order_items:
            print('ITEM:', item, type(item))
            item_name = item['item_name']
            quantity = item['quantity']

            new_item = get_or_create_item(item_name)

            order_item = OrderItem()
            order_item.item = new_item
            order_item.quantity = quantity
            order_item.save()

            order.order_items.add(order_item)

        #
        # response_data = {
        #     'order_number': order.order_number,
        #     status: status.HTTP_201_CREATED
        # }
        return Order.objects.filter(id=order.id)

        # return Order.objects.all()


def get_or_create_item(item_name):
    try:
        item = Item.objects.get(name=item_name)
    except Item.DoesNotExist:
        item = Item()
        item.name = item_name
        item.save()
    return item



# class OrderListCreate(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# @api_view(['POST'])
# @csrf_exempt
# def something(request, *args, **kwargs):
#     print('hitting this')
#     # print('*** data ***', request.__dict__)
#     print('*** method ***', request.method)
#     print('*** GET ***', request.GET)
#     print('*** POST ***', request.POST)
#     print('*** args ***', args)
#     print('*** kwargs ***', kwargs)
#
#     return HttpResponse("Hello World")

#
# class OrderCreate(APIView):
#
#     # def get(self, request):
#     #     date = self.request.query_params.get('date', None)
#     #     status = self.request.query_params.get('status', None)
#     #     count = OrderIssue.objects.filter(order__delivery_date=date, status=status).count()
#     #     return Response(1)
#
#     def post(self, request):
#         order_items = self.request.data.get('order_items', None)
#         print('**order_items ***********', order_items)
#
#         order = Order()
#         order.save()
#
#         for item in order_items:
#             # for key, value in item.items():
#             #     key = str(key)
#
#             # print('item', item, type(item))
#             # print('item.name', item.get('name'), type(item['name']))
#             # print('item.quantity', item.get('quantity'), type(item['quantity']))
#
#             item_name = item.get('name')
#             item_quantity = item.get('quantity')
#
#             new_item = get_or_create_item(item_name)
#
#             order_item = OrderItem()
#             order_item.item = new_item
#             order_item.quantity = item_quantity
#             order_item.save()
#
#             order.order_items.add(order_item)
#
#         response_data = {
#             'order_number': order.order_number,
#             status: status.HTTP_201_CREATED
#         }
#         return Response(response_data)



# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def create_order(request):
#     """
#     API View used to create an Order
#
#     :param request: POST with file and user id.
#     :return: Absolute URL of new image.
#     """
#     if request.method == 'POST':
#         print('***', request)
#         # user_id = request.data.get('user_id')
#         # file = request.data.get('file')
#         # u = User.objects.get(id=user_id)
#         # u.profile_picture = file
#         # u.save()
#         # image_url = request.build_absolute_uri(u.profile_picture.url)
#         return Response(request)


# @api_view(['POST'])
# # @permission_classes((IsAuthenticated,))
# def submit_order(request):
#     """
#     API View used to create an Order
#     :param request:
#     """
    # print('*****', request.__dict__)
#     # try:
#     # returned_item = ReturnedItem.objects.get(id=returned_item_id)
#     # returned_item.nonconformity_item = None
#     # returned_item.save()
#     return Response({'status': status.HTTP_200_OK})
#     # except Exception as e:
#     #     return Response({'error': str(e), 'status': status.HTTP_400_BAD_REQUEST})
#
