from django.conf.urls import include, url
from .views import *

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path

urlpatterns = [
    #url(r'^$', Hannovit.views.index, name='index'),
    url(r'^$', webpage),
    url(r'^search$', search)
]