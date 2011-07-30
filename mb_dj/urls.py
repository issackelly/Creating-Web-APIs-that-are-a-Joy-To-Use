from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from mb.api import ArtistResource, ArtistNameResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(ArtistResource())
v1_api.register(ArtistNameResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mb_dj.views.home', name='home'),
    # url(r'^mb_dj/', include('mb_dj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
