from django.contrib import admin
from .models import TagBlog

class tagblogAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'slug', 'timestamp']
    class Meta:
        model = TagBlog

admin.site.register(TagBlog, tagblogAdmin)