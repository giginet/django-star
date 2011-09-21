# -*- coding: utf-8 -*-
#    
#    api.handlers
#    created by giginet on 2011/09/20
#
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from piston.handler import BaseHandler
from piston.utils import rc, validate, throttle
from ..models import Star


def get_or_not_found(fn):
    """Get and set object or return rc.NOT_FOUND decorator
       Get object instance from content_type and object_id and set it to request.obj
       and call decorated function, or return rc.NOT_FOUND when object could not be found
    """
    def wrapper(self, request, content_type, object_id, *args, **kwargs):
        try:
            ctype = get_object_or_404(ContentType, pk=content_type)
            obj = ctype.get_object_for_this_type(pk=object_id)
            request.obj = obj
            return fn(self, request, content_type, object_id, *args, **kwargs)
        except (Http404, ObjectDoesNotExist):
            return rc.NOT_FOUND
    return wrapper

class StarHandler(BaseHandler):
    allowed_method = ('GET', 'POST', 'PUT', 'DELETE')
    model = Star
    fields = (
              'pk',
              'type',
              ('author', ('username', ), ),
              'comment'
    )
    
    @get_or_not_found
    def read(self, request, content_type, object_id):
        qs = self.model.objects.get_for_object(request.obj)
        return qs
    
    @get_or_not_found
    def create(self, request, content_type, object_id, tag=None, comment=None):
        qs = self.model.add_for_object(request.obj, request.user, tag, comment)