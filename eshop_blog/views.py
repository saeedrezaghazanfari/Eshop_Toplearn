from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog
from django.http import Http404

class ListBlog(ListView):
    template_name = 'blogs_list/blogs_list.html'
    def get_queryset(self):
        return Blog.objects.get_active_blog()
    paginate_by = 2

def blogDetail(request, *args , **kwargs):
    # print(kwargs['id'])
    blogs = Blog.objects.get_by_id(kwargs['id'])
    if blogs is None or not blogs.activeBlog:
        raise Http404('خبر مورد نظر شما پیدا نشد!')
    context = {'blog':blogs}
    return render(request , 'blogs_list/blog_detail.html' , context)

class Search_list_blog(ListView):
    template_name = 'blogs_list/blogs_list.html'
    paginate_by = 2
    def get_queryset(self):
        request = self.request
        query = request.GET.get('qB')
        if query is not None:
            return Blog.objects.search_blog(query)
        return Blog.objects.get_active_blog()
