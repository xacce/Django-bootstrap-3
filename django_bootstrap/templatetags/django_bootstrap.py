from django.template import Library

register = Library()
from django.forms.forms import BoundField
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper


@register.filter
def add_css_class(field, classes):
    try:
        trg = field.field.widget.widget
    except AttributeError:
        trg = field.field.widget
    if not trg.attrs.has_key('class'):
        trg.attrs['class'] = ''
    trg.attrs['class'] += ' %s' % classes
    return field


@register.assignment_tag
def get_content_type(object):
    from django.contrib.contenttypes.models import ContentType

    return ContentType.objects.get_for_model(object.__class__)


@register.filter
def fast_debug(var):
    print type(var)
    print var