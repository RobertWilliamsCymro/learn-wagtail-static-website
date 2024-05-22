from django import template
from wagtail.models import Page

register = template.Library()

@register.simple_tag
def get_navbar_pages():
    # return ['Item 1', 'Item 2', 'Item 3']
    return Page.objects.live().public().in_menu().filter(depth__gt=2)