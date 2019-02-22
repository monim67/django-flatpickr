from django import VERSION as DJANGO_VERSION
from django import get_version as get_django_version


def site_context(request):
    context = {
        'django_version': DJANGO_VERSION,
        'django_version_string': get_django_version(),
    }
    return context
