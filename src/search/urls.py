'''
Created on 2016. 11. 29.

@author: mskim
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^search$', views.search, name='search'),
    url(r'^report$', views.report, name='report'),
]