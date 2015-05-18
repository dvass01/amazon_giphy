from django.conf.urls import include, url,patterns
from django.contrib import admin
from interface.views import IndexView,LoginView,RegisterView,LogoutView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',

    url(r'^index',IndexView.as_view()),

    url(r'^register$', RegisterView.as_view()),

    url(r'^login$', LoginView.as_view()),

    url(r'^logout$',LogoutView.as_view()),

    # url(r'^my_page$', ClientView.as_view()),

    #gets

)
