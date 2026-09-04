"""Contains Base Date-Picker input class for widgets of this package."""

from typing import Any

from django import forms
from django.forms.widgets import DateTimeBaseInput

from ._config import WidgetConfig
from ._media import yield_css_files, yield_js_files
from .schemas import FlatpickrOptions, InputAttrs
from .settings import get_django_flatpickr_settings


class BasePickerInput(DateTimeBaseInput):
    """Base Date-Picker input class for widgets of this package."""

    picker_type = "DATE"
    datetime_format = "%Y-%m-%d"
    format_key = "DATE_INPUT_FORMATS"
    template_name = "django_flatpickr/input.html"
    options: FlatpickrOptions | None = None
    _option_overrides: dict[str, Any] | None = None

    def __init__(
        self,
        attrs: InputAttrs | None = None,
        *,
        options: FlatpickrOptions | None = None,
        range_from: str | None = None,
    ):
        """Initialize the Date-picker widget."""
        if not isinstance(options, (FlatpickrOptions, type(None))):
            raise ValueError("options must be of type FlatpickrOptions")
        if not isinstance(self.options, (FlatpickrOptions, type(None))):
            raise ValueError("options must be of type FlatpickrOptions")
        settings = get_django_flatpickr_settings()
        self.template_name = settings.template_name or self.template_name
        self.config = WidgetConfig(picker_type=self.picker_type, range_from=range_from)
        self.config.update_options(
            settings.options,
            self.options,
            options,
            overrides=self._option_overrides,
        )
        super().__init__(attrs, self.datetime_format)

    def build_attrs(
        self, base_attrs: InputAttrs, extra_attrs: InputAttrs | None = None
    ) -> InputAttrs:
        """Build an attribute dictionary."""
        settings = get_django_flatpickr_settings()
        attrs = {
            **settings.attrs,
            **base_attrs,
            **(extra_attrs or {}),
            "data-fpconfig": self.config.to_attr_value(),
        }
        if settings.debug:
            attrs["data-debug"] = ""
        return attrs

    @property
    def media(self) -> forms.Media:  # type: ignore
        """Generate widget Media."""
        settings = get_django_flatpickr_settings()
        return forms.Media(
            css={"all": tuple(yield_css_files(settings, self.config.options))},
            js=tuple(yield_js_files(settings, self.config.options)),
        )
