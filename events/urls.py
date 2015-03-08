from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'events.views.home', name='home'),
)
