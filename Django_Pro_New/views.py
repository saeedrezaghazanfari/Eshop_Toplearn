from django.contrib.auth import logout
from django.shortcuts import render, redirect
import itertools
from eshop_products.models import Product
from eshop_sliders.models import Slider
from eshop_site_setting.models import SiteSetting
from eshop_products_category.models import ProductCategory

# behiend code for render-partial
def header(request , *args , **kwargs):
    # a = request.META.get('PATH_INFO')
    site_setting = SiteSetting.objects.first()
    context = {
        'dataFromRenderPartial' : 'request.META.get("PATH_INFO")',
        # 'a': a
        'sitesetting':site_setting
    }
    return render(request , 'shared/_Header.html' , context)

# behiend code for render-partial
def footer(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'sitesetting':site_setting
    }
    return render(request , 'shared/_Footer.html' , context)    

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def home_page(request):
    sliders = Slider.objects.all()

    most_visits = Product.objects.order_by('-views').all()[:8]
    latest_prods = Product.objects.order_by('-id').all()[:8]

    categories = ProductCategory.objects.all()

    context = {
        'data' : 'this is data',
        'sliders': sliders,
        'most_visits': my_grouper(4, most_visits),
        'latest_prods': my_grouper(4, latest_prods),
        'categories':categories
    }
    return render(request , 'home_page.html' , context)

# def not_found(request):
#     context = {}
#     return render(request, '', context)

def Userlogout(request):
    logout(request)
    return redirect('/login')