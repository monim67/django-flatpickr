"""This module contains the widget classes."""

from flatpickr._base import BasePickerInput


__all__ = (
    'DatePickerInput',
    'TimePickerInput',
    'DateTimePickerInput',
)


class DatePickerInput(BasePickerInput):
    """
    Widget for DateField to display a Date-Picker Calendar.

    Args:
        - attrs (dict): HTML attributes of rendered HTML input
        - options (dict): Options to customize the widget, see Docs
    """

    picker_type = 'DATE'
    datetime_format = '%Y-%m-%d'
    format_key = 'DATE_INPUT_FORMATS'
    option_overrides = {
        'mode': 'single',
        'dateFormat': 'Y-m-d',
        'altInput': True,
    }


class TimePickerInput(BasePickerInput):
    """
    Widget for TimeField to display a Time-Picker Calendar.

    Args:
        - attrs (dict): HTML attributes of rendered HTML input
        - options (dict): Options to customize the widget, see Docs
    """

    picker_type = 'TIME'
    datetime_format = '%H:%M:%S'
    format_key = 'TIME_INPUT_FORMATS'
    option_overrides = {
        'mode': 'single',
        'dateFormat': 'H:i:S',
        'altInput': True,
        'enableTime': True,
        'noCalendar': True,
    }


class DateTimePickerInput(BasePickerInput):
    """
    Widget for DateTimeField to display a DateTime-Picker Calendar.

    Args:
        - attrs (dict): HTML attributes of rendered HTML input
        - options (dict): Options to customize the widget, see Docs
    """

    picker_type = 'DATETIME'
    datetime_format = '%Y-%m-%d %H:%M:%S'
    format_key = 'DATETIME_INPUT_FORMATS'
    option_overrides = {
        'mode': 'single',
        'dateFormat': 'Y-m-d H:i:S',
        'altInput': True,
        'enableTime': True,
    }
