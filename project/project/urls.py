from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^gvd/', include('client.urls')),
    url(r'^amazon/', include('amazon.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^giphy/', include('giphy.urls')),
)
