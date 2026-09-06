"""Datastructures of the package."""

from enum import Enum
from typing import Any, NoReturn, TypeAlias

from pydantic import BaseModel, ConfigDict, Field, field_validator

InputAttrs: TypeAlias = dict[str, Any]


class ThemeEnum(str, Enum):
    """Flatpickr theme options."""

    dark = "dark"
    material_blue = "material_blue"
    material_green = "material_green"
    material_red = "material_red"
    material_orange = "material_orange"
    airbnb = "airbnb"
    confetti = "confetti"


class FlatpickrOptions(BaseModel):
    """Flatpickr options to create flatpickr instance."""

    model_config = ConfigDict(extra="allow")

    allowInput: bool | None = None
    allowInvalidPreload: bool | None = None
    altFormat: str | None = None
    altInput: bool = True
    altInputClass: str | None = None
    ariaDateFormat: str | None = None
    clickOpens: bool | None = None
    dateFormat: str | None = None
    defaultDate: str | None = None
    defaultHour: int | None = Field(default=None, ge=0, le=23)
    defaultMinute: int | None = Field(default=None, ge=0, le=59)
    disable: list[str] | None = None
    disableMobile: bool | None = None
    enable: list[str] | None = None
    enableSeconds: bool | None = None
    enableTime: bool | None = None
    hourIncrement: int | None = Field(default=None, ge=1, le=12)
    inline: bool | None = None
    locale: str | None = None
    maxDate: str | None = None
    minDate: str | None = None
    minuteIncrement: int | None = Field(default=None, ge=0, le=59)
    mode: str | None = None
    monthSelectorType: str | None = None
    nextArrow: str | None = None
    noCalendar: bool | None = None
    position: str | None = None
    prevArrow: str | None = None
    shorthandCurrentMonth: bool | None = None
    showMonths: int | None = Field(default=None, ge=1, le=12)
    static: bool | None = None
    time_24hr: bool | None = None
    weekNumbers: bool | None = None
    wrap: bool = True

    @field_validator("mode")
    @classmethod
    def _disallow_mode(cls, v: str) -> NoReturn:
        raise ValueError(
            "Option mode is reserved and always set to static."
            " For range mode see how to use range picker in django-flatpickr docs"
        )

    @field_validator("dateFormat")
    @classmethod
    def _disallow_dateFormat(cls, v: str) -> NoReturn:
        raise ValueError(
            "Option dateFormat is reserved and always set to Y-m-d."
            " Use altFormat to set date format selected by calendar"
        )

    @field_validator("altInput")
    @classmethod
    def _disallow_altInput(cls, v: str) -> NoReturn:
        raise ValueError("Option altInput is reserved and always set to True.")

    @field_validator("wrap")
    @classmethod
    def _disallow_wrap(cls, v: str) -> NoReturn:
        raise ValueError("Option wrap is reserved and always set to True.")

    @field_validator("enableTime")
    @classmethod
    def _disallow_enableTime(cls, v: str) -> NoReturn:
        raise ValueError("Option enableTime is reserved and set based on widget used.")

    @field_validator("noCalendar")
    @classmethod
    def _disallow_noCalendar(cls, v: str) -> NoReturn:
        raise ValueError("Option noCalendar is reserved and set based on widget used.")
