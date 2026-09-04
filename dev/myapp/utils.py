from collections.abc import Callable
from typing import Any

from django.http import HttpResponse


def http_meta_redirect_view(url) -> Callable[[Any], HttpResponse]:
    """Return a meta redirect response."""
    return lambda _: HttpResponse(
        f'<META http-equiv="refresh" content="0;URL={url}">'
        f'<p>If you are not redirected automatically, follow this <a href="{url}">link</a>.</p>'
    )
