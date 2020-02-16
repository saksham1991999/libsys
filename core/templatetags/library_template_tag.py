from django import template
from core.models import library, bookmark, comparison

register = template.Library()


@register.filter
def added_to_bookmark(user, id):
    try:
        if user.is_authenticated:
            qs = bookmark.objects.filter(user=user)[0]
            # if qs.exists():
            if qs.libraries.filter(id=id).exists():
                return True
    except:
        return False


@register.filter
def added_to_compare(user, id):
    try:
        if user.is_authenticated:
            qs = comparison.objects.filter(user=user)[0]
            # if qs.exists():
            if qs.libraries.filter(id=id).exists():
                return True
    except:
        return False

