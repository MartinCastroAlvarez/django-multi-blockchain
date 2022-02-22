"""
A view function, or view for short, is a Python function that
takes a Web request and returns a Web response. This response
can be the HTML contents of a Web page, or a redirect, or a
404 error, or an XML document, or an image . . . or anything, really.
"""

import json

from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpRequest

from bnb.auth import distributed_login_required
from bnb.logic import AccountLogic


@distributed_login_required
@require_http_methods(['GET', ])
def get_balance(request: HttpRequest) -> HttpResponse:
    """
    Returns the details of the current user.
    """
    return HttpResponse(
        json.dumps({
            "wallet": request.user.username,
            "balance": AccountLogic.get_balance(request.user.username),
            "network": settings.LOCAL_SERVER_ID,
        }),
        content_type="application/json",
    )
