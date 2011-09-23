# -*- coding: utf-8 -*-
#    
#    api.urls
#    created by giginet on 2011/09/20
#
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.doc import documentation_view

from handlers import StarHandler

star_handler = Resource(StarHandler)

urlpatterns = patterns('',
    url(r'^get/(?P<content_type>\d+)/(?P<object_id>\d+)/$', star_handler, name='star-api-get'),
    url(r'^add/(?P<content_type>\d+)/(?P<object_id>\d+)/$', star_handler, name='star-api-add'),
    url(r'^delete/(?P<star_id>\d+)/$',                      star_handler, name='star-api-delete'),
    url(r'^doc/$', documentation_view),
)