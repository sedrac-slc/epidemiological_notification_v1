from django import template
from backend.entities.concrect.person import genders

register = template.Library()

@register.filter(name='gender_description')
def gender_description(value):
    return genders.get(value, value)