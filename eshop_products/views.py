from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, ProductGallery
from django.http import  Http404
from eshop_tag.models import Tag
from eshop_products_category.models import ProductCategory
from eshop_order.forms import OrderForm
import itertools

# def products(requset):
#     context = {}
#     return render(requset , 'products/products_list.html', context)

class Productlist(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3
    def get_queryset(self):
        return Product.objects.get_active_products()


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def productDetail(request, *args , **kwargs):
    S_productId = kwargs['id']
    # productName = kwargs['name']


    # Order
    orderForm = OrderForm(request.POST or None, initial={'product_id':S_productId})


    product: Product = Product.objects.get_by_id(S_productId)
    if product is None or not product.active:
        raise Http404('محصول مورد نظر پیدا نشد')

    # views
    product.views += 1
    product.save()

    galleries = ProductGallery.objects.filter(product_id=S_productId)
    group_gallery = list(my_grouper(3, galleries))

    related_products = Product.objects.filter(categories__product=product)
    group_related_products = list(my_grouper(3, related_products))

    tagsOfProducts = product.tag_set.all()

    context={
        'product': product,
        'tagsOfProducts': tagsOfProducts,
        'group_galleries': group_gallery,
        'group_related_products': group_related_products,
        'orderForm': orderForm,
    }

    return render(request , 'products/product_detail.html' , context)

class search_product_list(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3
    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()

class Product_categories_list(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('محصول مورد نظر یافت نشد')
        return Product.objects.get_product_category(category_name)

def products_category_partial(request):
    allOfCateGory = ProductCategory.objects.all()
    context = {'categories':allOfCateGory}
    return render(request, 'products/product_category_partial.html', context)