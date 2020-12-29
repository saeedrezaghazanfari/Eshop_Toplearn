from django.db import models

class SiteSetting(models.Model):
    title = models.CharField(max_length=120, verbose_name='نام سایت')
    address = models.CharField(max_length=120, verbose_name='آدرس')
    phone = models.CharField(max_length=120, verbose_name='تلفن تماس')
    fax = models.CharField(max_length=120, verbose_name='فکس')
    email = models.CharField(max_length=120, verbose_name='ایمیل')
    aboutus = models.TextField(verbose_name='درباره ما')
    logo = models.ImageField(verbose_name='لوگو ی سایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات سایت'

    def __str__(self):
        return self.title