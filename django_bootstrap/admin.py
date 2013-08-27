from django.contrib import admin
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.html import mark_safe
from django_bootstrap import widget as djbo_widgets
from django_bootstrap import forms as djbo_forms
from django.contrib.admin.widgets import AdminIntegerFieldWidget
from django.contrib import messages


class BaseAdminFormWidget(object):
    request = None
    object = None
    model_admin = None

    def __init__(self, request, model_admin, object=None):
        self.request = request
        self.object = object
        self.model_admin = model_admin

    @property
    def html(self):
        from django.template import loader, Context

        t = loader.get_template(self.template)
        c = Context(self.get_context())

        rend = t.render(c)
        return rend

    def get_context(self):
        return {}


class BaseAdminOverrides(object):
    _djbo_formfield_overrides = {
        models.TimeField: {'widget': djbo_widgets.TimeWidget},
        models.DateTimeField: {
            'form_class': forms.SplitDateTimeField,
            'widget': djbo_widgets.AdminSplitDateTime
        },
        models.DateField: {'widget': djbo_widgets.DateWidget},
        models.DecimalField: {
            'form_class': djbo_forms.AdminFloatField,
        }
    }

    def __init__(self, model, admin_site):
        super(BaseAdminOverrides, self).__init__(model, admin_site)
        self.formfield_overrides.update(self._djbo_formfield_overrides)


class BaseAdminTabular(BaseAdminOverrides, admin.TabularInline):
    pass


class BaseAdmin(BaseAdminOverrides, admin.ModelAdmin):
    image_preview_field = None
    objects_limit = None
    widgets = []
    admin_menu_group = (_(u'admin'), _(u'admin'))

    def get_limited_count(self):
        return self.model.objects.count()

    def add_view(self, request, *args, **kwargs):
        from django.http import HttpResponseRedirect
        from django.core.urlresolvers import reverse

        print self.objects_limit, self.get_limited_count()
        if self.objects_limit and self.objects_limit >= self.get_limited_count():
            messages.warning(request, _(u'Maximum reached for objects of this type'))

            return HttpResponseRedirect(reverse('admin:%s_%s_changelist' % (self.model._meta.app_label, self.model.__name__.lower())))

        return super(BaseAdmin, self).add_view(request, *args, **kwargs)

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['widgets'] = []
        for widget in self.widgets:
            widget_obj = widget(request, self, obj)
            context['widgets'].append(widget_obj)
            context['media'] += widget_obj.media
        return super(BaseAdmin, self).render_change_form(request, context, add, change, form_url, obj)

    def image_preview(self, obj):
        if hasattr(obj, self.image_preview_field):
            return '<img src="%s%s" class="list_preview_icon"/>' % (settings.MEDIA_URL, getattr(obj, self.image_preview_field))


    def change_list_bool_column(self, bool):
        q = ('<span class="glyphicon glyphicon-ok"></span>' if bool else '<span class="glyphicon glyphicon-minus"></span>')

        return mark_safe(q)

    image_preview.short_description = u''
    image_preview.allow_tags = True

    @property
    def media(self):
        return forms.Media()

