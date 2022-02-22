#from django.conf.urls import url
from django.urls import re_path
import dinamicform.views as views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^done/$', views.done),
]
