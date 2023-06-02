from django import template
from django.conf import settings

register = template.Library()


@register.filter(needs_autoescape=True)
def mediapath(image_path):
    return f"{settings.MEDIA_URL}{image_path}"