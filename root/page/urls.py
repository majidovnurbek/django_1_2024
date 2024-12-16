from django.urls import path
from page.views import *

urlpatterns = [
    path('',home,name="home"),
    path('post',post,name="post"),
]
