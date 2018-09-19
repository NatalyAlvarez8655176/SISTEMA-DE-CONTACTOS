# encoding:utf-8
from django import template
from django.apps import apps

from bookphone.models import Secretaria, Personal_secretaria, Personal_unidad
from bookphone.models import Unidad


register = template.Library()


@register.filter()
def to_int(value):
    return int(value)


@register.simple_tag
def get_unidad(id):
    return Unidad.objects.filter(secretaria=to_int(id)).order_by('name')


@register.simple_tag
def get_secretaria(id):
    return Secretaria.objects.get(id)


@register.simple_tag
def get_secretarias():
    return Secretaria.objects.order_by('name').all


@register.simple_tag
def get_personal(id):
    return Personal_secretaria.objects.filter(secretaria=to_int(id)).order_by('name')


@register.simple_tag
def get_personalu(id):
    return Personal_unidad.objects.filter(unidad=to_int(id)).order_by('name')


@register.simple_tag
def get_response_value(diagnose, formdiagnose, q):
    pass