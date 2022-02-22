"""
A view function, or view for short, is a Python function that
takes a Web request and returns a Web response. This response
can be the HTML contents of a Web page, or a redirect, or a
404 error, or an XML document, or an image . . . or anything, really.
"""

import json
from typing import Union, Optional

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import BadRequest
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User


@login_required
@require_http_methods(['GET', ])
def get_details(request: HttpRequest, wallet: str) -> HttpResponse:
    """
    Returns the details of a given Wallet.
    """
    return HttpResponse(
        json.dumps({
            "wallet": wallet,
        }),
        content_type="application/json",
    )


@login_required
@require_http_methods(['GET', ])
def get_session(request: HttpRequest) -> HttpResponse:
    """
    Returns the details of the authenticated User.
    """
    return HttpResponse(
        json.dumps({
            "wallet": request.user.username,
        }),
        content_type="application/json",
    )


@csrf_exempt
@require_http_methods(['POST', ])
def do_login(request: HttpRequest) -> Union[HttpResponse, BadRequest]:
    """
    Authenticates as a given wallet with a given password.
    If the wallet is not registered, it creates a new one.
    """
    data: dict = json.loads(request.body)
    wallet: str = data.get('wallet', '')
    password: str = data.get('password', '')
    if not wallet:
        raise BadRequest('Missing wallet')
    if not password:
        raise BadRequest('Missing wallet')
    user: Optional[User] = authenticate(request, username=wallet, password=password)
    if user is None:
        user: User = User()
        user.username = wallet
        user.set_password(password)
        user.save()
    login(request, user)
    return HttpResponse(
        json.dumps({
            "wallet": user.username,
        }),
        content_type="application/json",
    )
