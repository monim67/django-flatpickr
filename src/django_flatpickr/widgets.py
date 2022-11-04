"""Widgets for flatpickr inputs."""

from django_flatpickr._base import BasePickerInput

__all__ = (
    "DatePickerInput",
    "TimePickerInput",
    "DateTimePickerInput",
)


class DatePickerInput(BasePickerInput):
    """Widget for DateField to display a Date-Picker Calendar.

    Args:
        attrs: HTML attributes of rendered HTML input
        options: Options to customize the widget, see Docs
        range_from: Name of input to link for range selection
    """

    picker_type = "DATE"
    datetime_format = "%Y-%m-%d"
    format_key = "DATE_INPUT_FORMATS"


class TimePickerInput(BasePickerInput):
    """Widget for TimeField to display a Time-Picker Calendar.

    Args:
        attrs: HTML attributes of rendered HTML input
        options: Options to customize the widget, see Docs
        range_from: Name of input to link for range selection
    """

    picker_type = "TIME"
    datetime_format = "%H:%M:%S"
    format_key = "TIME_INPUT_FORMATS"
    _option_overrides = {
        "dateFormat": "H:i:S",
        "enableTime": True,
        "noCalendar": True,
    }


class DateTimePickerInput(BasePickerInput):
    """Widget for DateTimeField to display a DateTime-Picker Calendar.

    Args:
        attrs: HTML attributes of rendered HTML input
        options: Options to customize the widget, see Docs
        range_from: Name of input to link for range selection
    """

    picker_type = "DATETIME"
    datetime_format = "%Y-%m-%d %H:%M:%S"
    format_key = "DATETIME_INPUT_FORMATS"
    _option_overrides = {
        "dateFormat": "Y-m-d H:i:S",
        "enableTime": True,
    }
