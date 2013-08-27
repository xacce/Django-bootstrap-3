from django import forms
from django.templatetags.static import static

from django_bootstrap.admin import BaseAdminFormWidget
from django_bootstrap import models


class XploadImagesAdminWidget(BaseAdminFormWidget):
    template = 'django_bootstrap/xapload/images_inline.html'

    def get_context(self):
        from django.contrib.contenttypes.models import ContentType

        context = {'object': self.object}
        context['content_type'] = ContentType.objects.get_for_model(self.model_admin.model)
        if self.object:
            context['image_rels'] = models.XaploadImageRel.objects.filter(content_type=context['content_type'], object_id=self.object.pk)
        return context

    @property
    def media(self):
        return forms.Media(
            js=[static('django_bootstrap/xapload/init.js'), ],
            css={'screen': [static('django_bootstrap/xapload/main.css')]}
        )
