# -*- coding: utf-8 -*-
"""Contains Base Date-Picker input class for widgets of this package."""

from django.forms.widgets import DateTimeBaseInput
from flatpickr._settings import WidgetSettings
from flatpickr._media import WidgetMedia
from flatpickr._config import WidgetConfig


class BasePickerInput(DateTimeBaseInput):
    """Base Date-Picker input class for widgets of this package."""

    Media = WidgetMedia
    picker_type = 'DATE'
    datetime_format = '%Y-%m-%d'
    format_key = 'DATE_INPUT_FORMATS'
    option_overrides = {
        'dateFormat': 'Y-m-d',
    }

    def __init__(self, attrs=None, options=None):
        """Initialize the Date-picker widget."""
        self.config = WidgetConfig(self.picker_type)
        self.config._calculate_options(options, self.option_overrides)
        self.template_name = WidgetSettings.TEMPLATE_NAME or self.template_name
        _attrs = WidgetSettings.ATTRS.copy()
        _attrs.update(attrs or {})
        super().__init__(_attrs, self.datetime_format)

    def get_context(self, name, value, attrs):
        """Return widget context dictionary."""
        context = super().get_context(
            name, value, attrs)
        context['widget']['attrs']['fp_config'] = self.config.to_json()
        return context

    def start_of(self, event_id):
        """
        Set Date-Picker as the start-date of a date-range.

        Args:
            - event_id (string): User-defined unique id for linking two fields
        """
        WidgetConfig.events[str(event_id)] = self
        return self

    def end_of(self, event_id, import_options=True):
        """
        Set Date-Picker as the end-date of a date-range.

        Args:
            - event_id (string): User-defined unique id for linking two fields
        """
        event_id = str(event_id)
        if event_id in WidgetConfig.events:
            linked_picker = WidgetConfig.events[event_id]
            self.config.linked_to = linked_picker.config.id
        else:
            raise KeyError(
                'start-date not specified for event_id "%s"' % event_id)
        return self
