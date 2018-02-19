'''
from django.shortcuts import redirect
from django.conf import settings
import re

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, views_args, view_kwargs):
        assert hasattr(request,'user')

        if not request.user.is_authenicated():
            if True:
                return redirect(settings.LOGIN_URL)
'''
