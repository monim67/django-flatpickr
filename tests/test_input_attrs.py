from pytest_django.fixtures import SettingsWrapper

from django_flatpickr._base import BasePickerInput


def test_fpconfig_passed_to_input_attr() -> None:
    fp_input = BasePickerInput()
    assert "data-fpconfig" in fp_input.build_attrs({})


def test_presence_of_debug_attr_when_debug_true(settings: SettingsWrapper) -> None:
    settings.DEBUG = True
    fp_input = BasePickerInput()
    assert "data-debug" in fp_input.build_attrs({})


def test_absence_of_debug_attr_when_debug_false(settings: SettingsWrapper) -> None:
    settings.DEBUG = False
    fp_input = BasePickerInput()
    assert "data-debug" not in fp_input.build_attrs({})


def test_absence_of_debug_attr_when_debug_overrides(settings: SettingsWrapper) -> None:
    settings.DEBUG = True
    settings.DJANGO_FLATPICKR = {"debug": False}
    fp_input = BasePickerInput()
    assert "data-debug" not in fp_input.build_attrs({})
