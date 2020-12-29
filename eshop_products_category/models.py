from django.db import models

class ProductCategory(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    name = models.CharField(max_length=120, verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'دسته بندی (محصول)'
        verbose_name_plural = 'دسته بندی ها(محصول)'

    def __str__(self):
        return self.title

    def category_products(self):
        from eshop_products.models import Product
        prods = Product.objects.filter(categories__title=self.title, active=True)
        return prods