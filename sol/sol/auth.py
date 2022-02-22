"""
Authentication backends provide an extensible system for
when a username and password stored with the user model
need to be authenticated against a different service
than Django’s default.
"""

import requests

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.http import HttpRequest


def distributed_login_required(function: callable) -> callable:
    """
    Wrapper for validating that the request is authenticated.
    """

    def wrapper(request: HttpRequest, *args, **kwargs) -> callable:
        """
        Intercepts requests before they are passed into the view.
        Validates that the User exists in the SSO server.
        """
        cookies: dict = request.COOKIES
        url: str = settings.SSO_SERVER_SESSION_ENDPOINT
        response: dict = requests.get(url, cookies=cookies)
        if response.status_code == 200:
            session: dict = response.json()
            user: User = User()
            user.username = session['wallet']
            request.user = user
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    wrapper.__doc__ = function.__doc__
    wrapper.__name__ = function.__name__
    return wrapper
