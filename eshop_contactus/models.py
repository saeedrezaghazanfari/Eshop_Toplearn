from django.db import models

class contactus_model(models.Model):

    username = models.CharField(max_length=120, verbose_name='نام کاربری')
    email = models.CharField(max_length=120, verbose_name='ایمیل')
    subject = models.CharField(max_length=120, verbose_name='عنوان')
    msg = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(default=False, verbose_name='خوانده شده / نشده')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های کاربران'