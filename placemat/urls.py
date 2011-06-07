from django.conf.urls.defaults import patterns, url
from placemat import views

urlpatterns = patterns('',
    url(r'^fragments/(?P<path>.*)$', views.fragment, name="fragment")
)

