# -*- coding: utf-8 -*-
#    
#    templatetags.djangostar
#    created by giginet on 2011/09/23
#
from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.template.loader import render_to_string
from django.template import TemplateSyntaxError
from django.utils.translation import ugettext_lazy as _
import json

from ..models import Star

register = template.Library()

class RenderDjangoStarHeadNode(template.Node):
    def __init__(self, settings='{}'):
        self.settings = settings
        
    def render(self, context):
        settings_dict = json.loads(self.settings)
        settings_dict.update({'url' : {
                                       'add' : '/api/star/add/',
                                       'del' : '/api/star/del/',
                                       'get' : '/api/star/get/',
                                       }
                              }
        );
        settings = json.dumps(settings_dict)
        #settings = settings[1:len(settings)-1];
        context.push()
        html = render_to_string('star/head.html', {'settings' : settings}, context)
        context.pop()
        return html

class RenderDjangoStarListNode(template.Node):
    def __init__(self, object):
        print object
        self.object = template.Variable(object)
        
    def render(self, context):
        object = self.object.resolve(context)
        print object
        content_type = ContentType.objects.get_for_model(object)
        context.push()
        html = render_to_string('star/list.html', {'content_type' : content_type.pk, 'object_id' : object.pk }, context)
        context.pop()
        return html

@register.tag
def render_djangostar_head(parser, token):
    """Render javascript and css to be able the feature of editing tags
       Use this template tag in head block to be able the feature of editing tags.
       Syntax:
       {% render_djangostar_head %}
    """
    bits = token.split_contents()
    if len(bits) == 1:
        return RenderDjangoStarHeadNode()
    elif len(bits) == 2:
        return RenderDjangoStarHeadNode(bits[1])
    raise TemplateSyntaxError("%s tag takes 'setting' or no argument. " % bits[0])

@register.tag
def render_djangostar_list(parser, token):
    """Render universaltag list as ul list
    Usage:
        {% render_djangostar_list of <object> %}
    """
    bits = token.split_contents()
    if bits[1] != "of":
        raise TemplateSyntaxError("Second argument must be 'of'.")
    if len(bits) == 3:
        return RenderDjangoStarListNode(bits[2])
    raise TemplateSyntaxError("%s tag takes exactly 3 arguments." % bits[0])