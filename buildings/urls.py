from django.urls import path 
#from .views import Search
from .views import *


urlpatterns = [
    path('', HomeListAPIView.as_view(), name = 'home' ),
    path('<slug>/', HomeDetailAPIView.as_view(), name = 'home-detail' ),
    path('images/<slug>/', ImageView.as_view(), name = 'images' ),
    #path('search/', Search.as_view(), name = 'search' ),
]
