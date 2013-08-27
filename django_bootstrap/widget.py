from django import forms
from django.contrib.admin.templatetags.admin_static import static
from django.contrib.admin import widgets
from django.utils.safestring import mark_safe

#
# class FloatWidget(widgets.AdminTextInputWidget):
#     def render(self, name, value, attrs=None):
#         if not attrs:
#             attrs = {}
#         attrs['data-mask-digits']
#         html = super(FloatWidget, self).render(name, value, attrs)
#         return mark_safe()
#

class TimeWidget(widgets.AdminTimeWidget):
    @property
    def media(self):
        return forms.Media(js=[static("django_bootstrap/js/libs/timeentry.js")])

    def render(self, name, value, attrs=None):
        html = super(TimeWidget, self).render(name, value, attrs)

        return mark_safe('<div class="input-group"><span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>%s</div>' % html)


class DateWidget(widgets.AdminDateWidget):
    @property
    def media(self):
        print "AHAHAH"
        return forms.Media(
            js=[static("django_bootstrap/js/libs/zebra/js.js"), ],
            css={'screen': ["django_bootstrap/js/libs/zebra/css.css"], }
        )


class AdminSplitDateTime(forms.SplitDateTimeWidget):
    """
    A SplitDateTime Widget that has some admin-specific styling.
    """

    @property
    def media(self):
        return forms.Media(
            js=[static("django_bootstrap/js/libs/zebra/js.js"), ],
            css={'screen': ["django_bootstrap/js/libs/zebra/css.css"], }
        )

    def format_output(self, rendered_widgets):
        return mark_safe(u'<div class="row datetime_input"><div class="col-lg-3">%s</div>'
                         u'<div class="col-lg-2">%s</div></div>' % \
                         (rendered_widgets[0], rendered_widgets[1]))

        #

# class DateTimeWidget(widgets.AdminDateWidget):
#     @property
#     def media(self):
#         return forms.Media(
#             js=[static("django_bootstrap/js/libs/zebra/js.js"), ],
#             css={'screen': ["django_bootstrap/js/libs/zebra/css.css"], }
#         )
#
#     def render(self, name, value, attrs=None):
#         attrs['style'] = "display:none"
#         html = super(DateTimeWidget, self).render(name, value, attrs)
#         return html
#         #attrs['class'] = ''
#         #return mark_safe(
#         '<div class="row">%s<div class="col-lg-2"><input name="" class="vDateField form-control" type="text" id="%s_join" size="8"></div>'
#         #    '<div class="col-lg-1"><input name="" class="vTimeField form-control" type="text" id="%s_join" size="8"></div></div>' % (html, attrs['id'], attrs['id']))
