from django.contrib.contenttypes.models import ContentType
from django.views.generic import TemplateView, DetailView
from django.http import Http404
from django.core.urlresolvers import reverse
from django.conf import settings

from django_bootstrap.helpers.views import CSRFExempt, PostAsGet, ManuallyJsonResponse
import models


class UploadView(CSRFExempt, ManuallyJsonResponse, TemplateView):
    template_name = 'django_bootstrap/tmp.html'

    def post(self, request, *args, **kwargs):
        import os
        from uuid import uuid4
        # request.FILES.get('file')
        try:
            ct = ContentType.objects.get_for_id(self.kwargs.get('content_type_id', 0))
            object = ct.get_object_for_this_type(pk=self.kwargs.get('object_id', 0))
        except ContentType.DoesNotExist:
            raise Http404
        rel = models.XaploadImageRel(content_object=object)
        path = '%s.%s' % (str(uuid4()), 'jpg')
        rel.image.save(path, request.FILES.get('file'))
        rel.save()
        os.chmod(settings.ROOT_PATH + rel.image.url, 0755)
        return self.return_json({'delete_url': reverse('djbo_delete', args=(rel.pk,)), 'path': rel.image.url})


class DeleteImage(ManuallyJsonResponse, DetailView):
    def get(self, request, *args, **kwargs):
        try:
            ct = models.XaploadImageRel.objects.get(id=self.kwargs.get('pk'))
            ct.delete()
        except models.XaploadImageRel.DoesNotExist:
            raise Http404
        return self.return_json({})