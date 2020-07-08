from django.conf.urls import include, url
import Hannovit.views

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path

urlpatterns = [
    #url(r'^$', Hannovit.views.index, name='index'),
    #url(r'^$', Hannovit.views.webpage, name='webpage')
    url(r'^',include('Hannovit.urls'))
]