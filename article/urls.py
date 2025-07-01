from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main_Page, name='main_page'),
    path('articles/', article, name='article_list'),
    path('contact/', contact, name='contact'),
    path('articles/<int:id>/', article_detail, name='article_detail')
]


