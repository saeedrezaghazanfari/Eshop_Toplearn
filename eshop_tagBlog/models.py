from django.db import models
from eshop_blog.models import Blog

class TagBlog(models.Model):

    title = models.CharField(max_length=120 ,verbose_name='عنوان')
    slug = models.SlugField(verbose_name='عنوان در url')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='زمان')
    blogs = models.ManyToManyField(Blog, blank=True, verbose_name='لیست اخبار')

    class Meta:
        verbose_name = 'برچسب خبر'
        verbose_name_plural = 'برچسب اخبار'

    def __str__(self):
        return self.title