from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class XaploadImageRel(models.Model):
    image = models.ImageField(upload_to='media/')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveSmallIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')