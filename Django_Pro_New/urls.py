
from django.contrib import admin
from django.urls import path, include
from .views import home_page, header, footer, Userlogout

# import static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', home_page),
    path('Userlogout', Userlogout),

    # includes external urls
    path('', include('eshop_account.urls')),
    path('', include('eshop_products.urls')),
    path('', include('eshop_blog.urls')),
    path('', include('eshop_contactus.urls')),
    path('', include('eshop_site_setting.urls')),
    path('', include('eshop_order.urls')),
    path('api/v1/', include('eshop_API.urls')),

    # render_partial
    path('header', header, name="header"),
    path('footer', footer, name="footer"),

    # admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)