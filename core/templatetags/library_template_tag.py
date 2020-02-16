from django import template
from core.models import library, bookmark, comaprison

register = template.Library()


@register.filter
def added_to_bookmark(user, id):
    if user.is_authenticated:
        qs = bookmark.objects.filter(user=user)[0]
        # if qs.exists():
        if qs.libraries.filter(id=id).exists():
            return True
    return False


@register.filter
def added_to_compare(user, id):
    if user.is_authenticated:
        qs = comaprison.objects.filter(user=user)[0]
        # if qs.exists():
        if qs.libraries.filter(id=id).exists():
            return True
    return False

