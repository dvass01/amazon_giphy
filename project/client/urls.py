from django.conf.urls import include, url

urlpatterns = [
    url(r'^api/words/(?P<phrase>[\w\']+$', 'client.views.get_random_word', name='get_random_word'),
]
