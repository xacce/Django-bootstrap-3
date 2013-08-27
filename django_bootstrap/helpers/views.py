import json
from django import http
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.admin.views.decorators import staff_member_required


class StaffRequired(object):
    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(StaffRequired, self).dispatch(*args, **kwargs)


class LoginRequired(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequired, self).dispatch(*args, **kwargs)


class FormBasedWithRequest(object):
    def get_form_kwargs(self):
        i = super(FormBasedWithRequest, self).get_form_kwargs()
        i['request'] = self.request
        return i


class ManuallyJsonResponse(object):
    def return_json(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        return json.dumps(context)


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        return json.dumps(context)


class CSRFExempt(object):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CSRFExempt, self).dispatch(request, *args, **kwargs)


class PostAsGet(object):
    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)