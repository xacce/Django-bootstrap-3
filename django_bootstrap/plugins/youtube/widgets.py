from django.forms.widgets import TextInput


class YoutubeFieldWidget(TextInput):
    attrs = None

    def __init__(self, attrs=None):
        default = {'class': 'youtube_field'}
        if attrs:
            default.update(attrs)
        super(YoutubeFieldWidget, self).__init__(default)

    def render(self, name, value, attrs=None):
        from django.template.loader import render_to_string
        import re

        video_id = None
        if value:
            q = re.search(r'^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*', value, re.UNICODE)
            if q:
                video_id = q.group(7)

        input_html = super(YoutubeFieldWidget, self).render(name, value, attrs)
        html = render_to_string('django_youtube_field/field.html', {'input': input_html, 'video_id': video_id})
        return html

    class Media:
        js = ('django_youtube_field/init.js',)