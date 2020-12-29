from django.urls import path
from .views import contactUsPage

urlpatterns = [
    path('contactus/', contactUsPage)
]