from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^state/(\d+)/', views.state, name='state')
]