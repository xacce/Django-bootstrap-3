class YoutubeAdmin(object):
    def formfield_for_dbfield(self, db_field, **kwargs):
        from django_bootstrap.plugins.youtube.fields import YoutubeField
        from django_bootstrap.plugins.youtube.widgets import YoutubeFieldWidget

        if isinstance(db_field, YoutubeField):
            kwargs['widget'] = YoutubeFieldWidget

        field = super(YoutubeAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        return field


# class YoutubeAdminTabularInline(object)