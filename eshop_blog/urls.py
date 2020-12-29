
from django.urls import path
from .views import ListBlog, blogDetail, Search_list_blog

urlpatterns = [
    path('blog', ListBlog.as_view()),
    path('blog/<id>/<name>/<GOOD>', blogDetail),
    path('blog/search', Search_list_blog.as_view()),
]
