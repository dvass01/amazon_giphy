from django.conf.urls import include, url,patterns
from django.contrib import admin
from client.views import IndexView,LoginView,RegisterView,LogoutView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',

    url(r'^index',IndexView.as_view()),

    url(r'^register$', RegisterView.as_view()),

    url(r'^login$', LoginView.as_view()),

    url(r'^logout$',LogoutView.as_view()),

    url(r'^api/words/(?P<phrase>[\w\']+$', 'client.views.get_random_word', name='get_random_word'),

)
