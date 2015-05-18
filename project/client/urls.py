from django.conf.urls import include, url,patterns
from django.contrib import admin
from client.views import IndexView,LoginView,RegisterView,LogoutView,PlayView,GameView


urlpatterns = patterns('',

    url(r'^index',IndexView.as_view()),

    url(r'^register$', RegisterView.as_view()),

    url(r'^login$', LoginView.as_view()),

    url(r'^logout$',LogoutView.as_view()),

    url(r'^play$',PlayView.as_view()),

    url(r'^play/game',GameView.as_view()),
)
