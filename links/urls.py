from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<token>[^/]+)$', 'links.views.lookup', name='link_token_lookup'),
)
