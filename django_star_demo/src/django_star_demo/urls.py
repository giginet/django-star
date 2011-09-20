from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

admin.autodiscover()
  
urlpatterns = patterns('',
    (r'^admin/',                       include(admin.site.urls)),
    (r'^blogs/',                       include('django_star_demo.blogs.urls')),
    url(r'^$',                         TemplateView.as_view(template_name="index.html"), name='index'),
)