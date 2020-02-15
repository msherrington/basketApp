from django.contrib import admin
from django.urls import path

from items import views as item_views
from orders import views as order_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/submit-order', order_views.OrderViewSet.as_view({'post': 'list'})),
    path('api/items/', item_views.ItemList.as_view()),
]
