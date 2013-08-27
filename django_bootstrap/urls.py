# from django.conf import settings
from django.conf.urls.defaults import patterns, url
#
# urls = []
# if 'admin_tools.menu' in settings.INSTALLED_APPS:
#     urls.append(url(r'^menu/', include('admin_tools.menu.urls')))
# if 'admin_tools.dashboard' in settings.INSTALLED_APPS:
#     urls.append(url(r'^dashboard/', include('admin_tools.dashboard.urls')))
#
# urlpatterns = patterns('', *urls)
import views

urlpatterns = patterns('',
                       url(r'^upload/(?P<content_type_id>\d+)/(?P<object_id>\d+)$', views.UploadView.as_view(), name='djbo_upload'),
                       url(r'^delete/(?P<pk>\d+)$', views.DeleteImage.as_view(), name='djbo_delete'),
)
