# -*- coding: utf-8 -*-
#    
#    api.handlers
#    created by giginet on 2011/09/20
#
from piston.handler import BaseHandler
from piston.utils import rc, validate, throttle
from ..models import Star

class StarHandler(BaseHandler):
    allowed_method = ('GET', 'POST', 'PUT', 'DELETE')
    model = Star
    fields = (
              'pk',
              'color',
              'author',
              'comment'
    )