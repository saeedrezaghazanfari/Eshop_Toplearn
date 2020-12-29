from django.contrib import admin
from .models import Product, ProductGallery

class adminProduct(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']
    class Meta:
        model = Product

admin.site.register(Product, adminProduct)
admin.site.register(ProductGallery)
