from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = patterns(''
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gvd/', include('client.urls')),
    url(r'^amazon/', include('amazon.urls')),
    url(r'^giphy/', include('giphy.urls')),
)
