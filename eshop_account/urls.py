
from django.urls import path
from .views import login_user, register_user, user_edit, user

urlpatterns = [
    path('login/', login_user),
    path('register/', register_user),
    path('user', user),
    path('user/edit', user_edit),

]
