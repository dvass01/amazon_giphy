from django.conf.urls import url

urlpatterns = [
    url(r'^api/(?P<phrase>[\w\']+)$', 'amazon.views.get_dvd_cover_url', name='get_dvd_cover_url'),
]
