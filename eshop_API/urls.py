from django.urls import path
from .serializers import (

    GetAllAPI,
    GetFavAPI,
    UpdateFavData,
    PostData,
    SearchData,
    DeleteData,
)
urlpatterns = [
    path('get-all-data/', GetAllAPI),
    path('get-fav-data/', GetFavAPI.as_view()),
    path('update-fav-data/<int:pk>', UpdateFavData.as_view()),
    path('post-data/', PostData.as_view()),
    path('search/', SearchData.as_view()),
    path('delete-data/<int:pk>', DeleteData.as_view()),
]