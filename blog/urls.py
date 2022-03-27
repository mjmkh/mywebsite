from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog', blog_view, name='index'),
    path('single', blog_single, name='single')
]
