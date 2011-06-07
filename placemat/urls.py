from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^fragments/(?P<path>.*)$', views.fragment, name="fragment")
)

