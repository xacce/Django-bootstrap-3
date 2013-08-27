from django import forms
from django.contrib import admin
#
#
# class AdminForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AdminForm, self).__init__(*args, **kwargs)
#         for f in self.fields:
#             print type(f)


class AdminFloatField(forms.fields.DecimalField):
    def widget_attrs(self, widget):
        return {
            "data-digits": self.max_digits,
            "data-decimal-places": self.decimal_places,
            'class':'vDecimalField'
        }

        # def formfield(self, **kwargs):
        #     print 2
        #     if kwargs.has_key('widget'):
        #         print 3
        #         kwargs['widget'] = kwargs['widget'](attrs={
        #             "data-digits": self.max_digits,
        #             "data-decimal-places": self.decimal_places,
        #         })
        #     return super(AdminFloatField, self).formfield(**kwargs)