from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from blogs.models import Entry
import os

admin.autodiscover()

class IndexView(TemplateView):
    template_name = r'index.html'

    def get_context(self, *args, **kwargs):
        context = super(IndexView, self).get_context(*args, **kwargs)
        context['object'] = Entry.objects.get(pk=1)
        return context

urlpatterns = patterns('',
    (r'^admin/',                       include(admin.site.urls)),
    (r'^blogs/',                       include('django_star_demo.blogs.urls')),
    (r'^api/star/',                    include('star.api.urls')),
    url(r'^$',                         TemplateView.as_view(template_name="index.html"), name='index'),
)

document_root = lambda x: os.path.join(os.path.dirname(__file__), x)
urlpatterns += patterns('django.views.static',
    (r'^css/(?P<path>.*)$', 'serve', {'document_root': document_root('../../static/css')}),
    (r'^js/(?P<path>.*)$',  'serve', {'document_root': document_root('../../static/js')}),
    (r'^img/(?P<path>.*)$', 'serve', {'document_root': document_root('../../static/img')}),
)
