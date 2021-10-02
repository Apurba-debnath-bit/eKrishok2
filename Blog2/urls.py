

from django.urls.conf import path
from django.urls.resolvers import URLPattern
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.homeBlog, name='home_Blog'),
    path('blog-detail/<slug>' , blog_detail , name="blog_detail"),
    path('category/<slug:url>',category),
    path('detail/<slug:slug>',PostDetail),

]