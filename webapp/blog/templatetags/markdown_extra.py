from django import template
from django.template.defaultfilters import stringfilter
import markdown as md
import bleach

register = template.Library()

@register.filter()
@stringfilter
def markdown(value: str):

    return bleach.linkify(md.markdown(bleach.clean(value)))
