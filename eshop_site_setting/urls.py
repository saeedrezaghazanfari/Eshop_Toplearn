from django.urls import path
from .views import siteSetting_page

urlpatterns = [
    path('about-us/', siteSetting_page)
]