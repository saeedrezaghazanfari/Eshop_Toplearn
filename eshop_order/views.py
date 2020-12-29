from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order, OrderDetail
from eshop_products.models import Product
from django.contrib import messages

# ZARIN PAL import
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client


@login_required(login_url='/login')
def add_user_order(request):

    new_order_form = OrderForm(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id= request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data.get('count')
        if count <= 0:
            count = 1
        product = Product.objects.get_by_id(productId=product_id)

        order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)

        # return redirect('/user/orders')
        return redirect('/open-order')

    return redirect('/')

@login_required(login_url='/login')
def crease_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('orderDetail_id')
    if detail_id:
        order_add = OrderDetail.objects.get(id=detail_id, order__owner_id=request.user.id)
        if order_add:
            order_add.count += 1
            order_add.save()
            return redirect('/open-order')

@login_required(login_url='/login')
def deCrease_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('orderDetail_id')
    if detail_id:
        order_min = OrderDetail.objects.get(id=detail_id, order__owner_id=request.user.id)
        if order_min:
            order_min.count = order_min.count -1
            if order_min.count < 1:
                order_min.count = 1
                order_min.save()
            messages.info(request, 'نمیتوان محصول منفی داشت')
            order_min.save()
            return redirect('/open-order')

@login_required(login_url='/login')
def remove_order_detail(request, *args, **kwargs):
    order_detail = kwargs.get('orderDetail_id')
    if order_detail is not None:
        exist = OrderDetail.objects.get(order__owner_id=request.user.id, id=order_detail)
        if exist:
            exist.delete()
            return redirect('/open-order')

@login_required(login_url='/login')
def open_order(request):
    context = {
        'order': None,
        'details': None,
        'total': 0
    }
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total'] = open_order.get_toatal_price()

    return render(request, 'open_order.html', context)


# ZARIN PAL CODES

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional

client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
CallbackURL = 'http://localhost:8000/verify' # Important: need to edit for realy server.

def send_request(request):
    total_price = 0
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if open_order is not None:
        total_price = open_order.get_toatal_price()

        result = client.service.PaymentRequest(
            MERCHANT,
            total_price,
            description,
            email,
            mobile,
            f'{CallbackURL}/{open_order.id}'
        )
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            return HttpResponse('Error code: ' + str(result.Status))


def verify(request, *args, **kwargs):

    order_id = kwargs.get('order_id')

    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            user_order = Order.objects.get(id=order_id)
            user_order.is_paid = True
            user_order.payment_date = time.time()
            user_order.save()

            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))

        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
