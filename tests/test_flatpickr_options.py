import pytest

from django_flatpickr._base import BasePickerInput
from django_flatpickr.schemas import FlatpickrOptions


def test_invalid_options_shouldnt_be_set_as_class_property() -> None:
    class TestInput(BasePickerInput):
        options = "Not a FlatpickrOptions instance"  # type: ignore

    with pytest.raises(ValueError):
        TestInput()


def test_invalid_options_shouldnt_be_passed_as_parameter() -> None:
    with pytest.raises(ValueError):
        BasePickerInput(options="Not a FlatpickrOptions instance")  # type: ignore


def test_reserved_options_shouldnt_be_set_by_user() -> None:
    with pytest.raises(ValueError):
        FlatpickrOptions(mode="range")
    with pytest.raises(ValueError):
        FlatpickrOptions(dateFormat="Y")
    with pytest.raises(ValueError):
        FlatpickrOptions(enableTime=False)
    with pytest.raises(ValueError):
        FlatpickrOptions(noCalendar=False)
    with pytest.raises(ValueError):
        FlatpickrOptions(altInput=False)
    with pytest.raises(ValueError):
        FlatpickrOptions(wrap=False)
