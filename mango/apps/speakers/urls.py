from django.conf.urls import patterns, url


urlpatterns = patterns('speakers.views',
    url(r'^$', 'list', name='speakers_list'),
)
