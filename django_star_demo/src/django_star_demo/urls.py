from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
import os

admin.autodiscover()
  
urlpatterns = patterns('',
    (r'^admin/',                       include(admin.site.urls)),
    (r'^blogs/',                       include('django_star_demo.blogs.urls')),
    (r'^api/star/',                 include('star.api.urls')),
    url(r'^$',                         TemplateView.as_view(template_name="index.html"), name='index'),
)

document_root = lambda x: os.path.join(os.path.dirname(__file__), x)
urlpatterns += patterns('django.views.static',
    (r'^css/(?P<path>.*)$', 'serve', {'document_root': document_root('../../static/css')}),
    (r'^js/(?P<path>.*)$', 'serve', {'document_root': document_root('../../static/js')}),
    (r'^img/(?P<path>.*)$', 'serve', {'document_root': document_root('../../static/img')}),
)