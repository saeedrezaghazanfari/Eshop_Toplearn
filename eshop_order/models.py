from django.contrib.auth.models import User
from django.db import models

from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='مالک')
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()

    def get_toatal_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید مربوطه')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت')
    count = models.IntegerField(verbose_name='تعداد')

    def get_abs_price(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'جزئیات سبد خرید'
        verbose_name_plural = 'جزئیات سبد های خرید کاربران'

    def __str__(self):
        return self.product.title
