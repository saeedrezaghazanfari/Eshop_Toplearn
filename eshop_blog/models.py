from django.db import models
from django.core import validators
from django.db.models import Q

class BlogManager(models.Manager):
    def get_active_blog(self):
        return self.get_queryset().filter(activeBlog=True)
    def get_by_id(self, blog_id):
        qs = self.get_queryset().filter(id=blog_id)
        if qs.count() == 1:
            return qs.first()
        return None
    def search_blog(self ,query):
        lookup = (
            Q(titleBlog__icontains=query) |
            Q(descriptionBlog__icontains=query) |
            Q(tagblog__title__icontains=query)
        )
        return self.get_queryset().filter(lookup ,activeBlog=True)

class Blog(models.Model):

    userBlog = models.CharField(max_length=20 , verbose_name='نام کاربر تولیدکننده ی محتوا',
    validators=[
        validators.MinLengthValidator(limit_value=3, message='no this is little'),
        validators.MaxLengthValidator(limit_value=20 , message='no this is big')
    ])
    titleBlog = models.CharField(max_length=120 ,verbose_name='عنوان خبر')
    descriptionBlog = models.TextField(verbose_name='متن خبر')
    imageBlog = models.ImageField(null=False , blank=False,verbose_name='تصویر خبر')
    activeBlog = models.BooleanField(default=False ,verbose_name='نمایش/روح')
    timeBlog = models.DateTimeField(auto_now_add=True)

    objects = BlogManager()

    class Meta:
        verbose_name= 'خبر'
        verbose_name_plural = 'اخبار'

    def __str__(self):
        return self.titleBlog

    def get_url_abs(self):
        return f'/blog/{self.id}/{self.titleBlog.replace(" ","-")}/SAEEDREZA--BLOGS'