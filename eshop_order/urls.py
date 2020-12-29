from django.urls import path
from .views import add_user_order, open_order, send_request, verify, remove_order_detail, crease_order_detail, deCrease_order_detail

urlpatterns = [
    path('add-user-order', add_user_order),
    path('open-order', open_order),
    path('remove-order-detail/<int:orderDetail_id>', remove_order_detail),
    path('request', send_request, name='request'),
    path('verify/<int:order_id>', verify, name='verify'),
    path('crease-order-detail/<int:orderDetail_id>', crease_order_detail),
    path('deCrease-order-detail/<int:orderDetail_id>', deCrease_order_detail),
]