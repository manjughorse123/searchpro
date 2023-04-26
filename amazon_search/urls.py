from django.urls import path
from .views import amazon_search

urlpatterns = [
    path('amazon_search/', amazon_search, name='search_amazon'),
]
