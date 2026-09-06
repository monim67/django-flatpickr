"""Tests for settings."""

from pydantic.fields import FieldInfo
from pytest_django import Settings

from django_flatpickr.settings import DjangoFlatpickrSettings, _DjangoSettingsSource


def test_django_settings_source_get_field_value(settings: Settings) -> None:
    """Test _DjangoSettingsSource get_field_value method."""
    source = _DjangoSettingsSource(DjangoFlatpickrSettings)
    settings.DJANGO_FLATPICKR = {"template_name": "custom.html"}

    value, field_name, flag = source.get_field_value(FieldInfo(), "template_name")
    assert value == "custom.html"
    assert field_name == "template_name"
    assert flag is False

    value, field_name, flag = source.get_field_value(FieldInfo(), "non_existent")
    assert value is None
    assert field_name == "non_existent"
    assert flag is False


def test_django_settings_source_get_field_value_no_config(settings: Settings) -> None:
    """Test _DjangoSettingsSource get_field_value when no DJANGO_FLATPICKR config exists."""
    source = _DjangoSettingsSource(DjangoFlatpickrSettings)
    if hasattr(settings, "DJANGO_FLATPICKR"):
        del settings.DJANGO_FLATPICKR

    value, field_name, flag = source.get_field_value(FieldInfo(), "template_name")
    assert value is None
    assert field_name == "template_name"
    assert flag is False


def test_django_settings_source_call(settings: Settings) -> None:
    """Test _DjangoSettingsSource __call__ method."""
    source = _DjangoSettingsSource(DjangoFlatpickrSettings)

    test_config = {"template_name": "custom.html"}
    settings.DJANGO_FLATPICKR = test_config
    assert source() == test_config

    del settings.DJANGO_FLATPICKR
    assert source() == {}
