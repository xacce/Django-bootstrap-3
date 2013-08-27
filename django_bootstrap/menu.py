# coding: utf-8
from admin_tools.menu import DefaultMenu

from django.core.urlresolvers import reverse, ResolverMatch
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from admin_tools.menu import items
from admin_tools.utils import get_admin_site
from django.core.urlresolvers import resolve


class DefaultMenu(DefaultMenu):
    request = None

    def init_with_context(self, context):
        self.request = context['request']
        resolved = resolve(context['request'].path)

        admin_site = get_admin_site(context['request'])
        grouped = {}
        for model, model_admin in admin_site._registry.items():
            if not context['request'].user.has_perm('%s.change_%s' % (model._meta.app_label, model.__name__.lower())):
                continue
            if hasattr(model_admin, 'admin_menu_group'):
                group_data = getattr(model_admin, 'admin_menu_group')
                if not group_data[0] in grouped:
                    grouped[group_data[0]] = CustomMenuItem(title=group_data[1], url="#")
                path = "%s_%s_" % (model._meta.app_label, model.__name__.lower())
                title = ugettext(model.__name__)
                css_classes = []
                if hasattr(model_admin, 'admin_menu_count'):
                    count = model_admin.admin_menu_count(model)
                    if count > 0:
                        title = '%s (%d)' % (title, count)
                        css_classes = ['bold', 'count']
                        grouped[group_data[0]].css_classes = ['bold']
                item = CustomMenuItem(title=title, url=reverse("admin:%s_%s_changelist" % (model._meta.app_label, model.__name__.lower())), css_classes=css_classes)
                if hasattr(resolved, 'url_name') and resolved.url_name.find(path) == 0:
                    item.force_selected = True
                grouped[group_data[0]].children.append(item)
            else:
                grouped[model._meta.app_label] = CustomMenuItem(title=model.__name__, url=reverse("admin:%s_%s_changelist" % (model._meta.app_label, model.__name__.lower())))

        if context['request'].user.is_superuser:
            if not grouped.has_key('community'):
                grouped['community'] = CustomMenuItem(u'Сообщество', url='#')
                grouped['community'].children.append(CustomMenuItem(title=u"Пользователи", url=reverse('admin:auth_user_changelist')))
                grouped['community'].children.append(CustomMenuItem(title=u"Группы", url=reverse('admin:auth_group_changelist')))
        if hasattr(self, 'update_menu'):
            grouped = getattr(self, 'update_menu')(grouped)
        self.children += grouped.values()


class CustomMenuItem(items.MenuItem):
    force_selected = False


    def is_selected(self, request):
        return super(CustomMenuItem, self).is_selected(request) if not self.force_selected else True
