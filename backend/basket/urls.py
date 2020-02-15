from django.contrib import admin
from django.urls import path

from orders import views as order_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/submit-order', order_views.OrderViewSet.as_view({'post': 'list'})),
]
