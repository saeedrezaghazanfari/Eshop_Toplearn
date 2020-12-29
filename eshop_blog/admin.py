from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['__str__' , 'titleBlog' ,'userBlog', 'activeBlog' , 'imageBlog']
    class Meta:
        model = Blog

admin.site.register(Blog, BlogAdmin)