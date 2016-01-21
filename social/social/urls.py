from django.conf.urls import patterns, include, url
from django.contrib import admin
from sapp.facebook import facebook_view
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^$', 'sapp.views.home'),
    url(r'^login/$', 'sapp.views.home'),
    url(r'^another-login-url/$', 'sapp.views.done'),
)