# -*- coding: utf-8 -*-
#    
#    django_star_demo.blogs.urls
#    created by giginet on 2011/09/20
#
from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView
from models import Entry

urlpatterns = patterns('',
    url('^(?P<pk>\d+)/$', DetailView.as_view(model=Entry), name="blogs-entry-detail"),
)