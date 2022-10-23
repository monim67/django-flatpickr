from typing import Iterable

from django_flatpickr.schemas import FlatpickrOptions
from django_flatpickr.settings import DjangoFlatpickrSettings


def yield_js_files(
    settings: DjangoFlatpickrSettings, options: FlatpickrOptions
) -> Iterable[str]:
    """Yield JavaScript media files for the widget."""
    yield settings.flatpickr_cdn_url + "flatpickr.min.js"
    yield settings.app_static_url + "js/django-flatpickr.js"
    if options.locale:
        yield settings.flatpickr_cdn_url + f"l10n/{options.locale}.js"


def yield_css_files(
    settings: DjangoFlatpickrSettings, options: FlatpickrOptions
) -> Iterable[str]:
    """Yield CSS media files for the widget."""
    yield settings.flatpickr_cdn_url + "flatpickr.min.css"
    if settings.theme_url:
        yield settings.theme_url
    elif settings.theme_name:
        yield settings.flatpickr_cdn_url + f"themes/{settings.theme_name.value}.css"
