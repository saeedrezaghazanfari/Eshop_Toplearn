
from django.urls import path
from .views import (
    Productlist,
    productDetail,
    search_product_list,
    Product_categories_list,
    products_category_partial,
)

urlpatterns = [
    path('products/', Productlist.as_view()),
    path('products/<id>/<name>/<GOOD>', productDetail),
    path('products/search', search_product_list.as_view()),
    path('products/<category_name>', Product_categories_list.as_view()),
    path('products-categories-partial', products_category_partial, name='pro_cat_par'),
]
