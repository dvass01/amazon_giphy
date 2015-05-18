from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = patterns(''
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clients/', include(admin.site.urls)),
    url(r'^gvd/', include('client.urls'),
)
