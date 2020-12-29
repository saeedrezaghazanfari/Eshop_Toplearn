from django.db import models
import os
from django.db.models import Q
from eshop_products_category.models import ProductCategory

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

def upload_Gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/Gallery/{final_name}"

class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self ,productId):
        qs = self.get_queryset().filter(id=productId)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self,query):
        lookup = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tag__title__icontains=query)
        )
        return  self.get_queryset().filter(lookup, active=True).distinct()

    def get_product_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

class Product(models.Model):

    title = models.CharField(max_length=30, verbose_name='عنوان')
    description = models.TextField( verbose_name='توضیحات محصول')
    price = models.IntegerField( verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True, verbose_name='تصویر محصول')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    categories = models.ManyToManyField( ProductCategory, blank=True, verbose_name='دسته بندی محصول')
    timestamp = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, verbose_name='بازدید ها')

    objects = ProductsManager()

    class Meta:
        verbose_name= 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}/peaka_url"

class ProductGallery(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_Gallery_image_path, blank=True, null=True, verbose_name='تصویر محصول')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'گالری'
        verbose_name_plural = 'گالری ها'

    def __str__(self):
        return self.title