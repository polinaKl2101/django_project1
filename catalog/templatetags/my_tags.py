from django import template

register = template.Library()


@register.filter(needs_autoescape=True)
def mediapath():
    pass