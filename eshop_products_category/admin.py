from django.contrib import admin
from .models import ProductCategory

class productCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'active']
    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, productCategoryAdmin)