from django.conf.urls.defaults import patterns, include, url
from placematt.urls import urlpatterns as placemat_patterns


urlpatterns = patterns('',
) + placemat_patterns

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)
