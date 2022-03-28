from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('products', products_view, name='products'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('single-product', single_product_view, name='single-product')
]
