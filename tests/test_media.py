from pytest_django.fixtures import SettingsWrapper

from django_flatpickr._base import BasePickerInput
from django_flatpickr.schemas import FlatpickrOptions


def test_media_render_with_default_options() -> None:
    fp_input = BasePickerInput()
    fp_input.media.render()


def test_presence_of_theme_url_in_rendered_media(settings: SettingsWrapper) -> None:
    theme_url = "http://localhost/xxxxxx"
    settings.DJANGO_FLATPICKR = {"theme_url": theme_url}
    fp_input = BasePickerInput()
    assert theme_url in fp_input.media.render()


def test_presence_of_local_file_in_rendered_media() -> None:
    locale = "xxxxxx"
    fp_input = BasePickerInput(options=FlatpickrOptions(locale=locale))
    assert locale in fp_input.media.render()
