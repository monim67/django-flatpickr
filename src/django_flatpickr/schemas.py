"""Datastructures of the package."""

from enum import Enum
from typing import Any, Dict, List, NoReturn, Optional

try:
    from pydantic.v1 import BaseModel, Extra, Field, validator
except ModuleNotFoundError:  # pragma: no cover
    from pydantic import BaseModel, Extra, Field, validator  # type: ignore

from typing_extensions import TypeAlias

InputAttrs: TypeAlias = Dict[str, Any]


class ThemeEnum(str, Enum):
    """Flatpickr theme options."""

    dark = "dark"
    material_blue = "material_blue"
    material_green = "material_green"
    material_red = "material_red"
    material_orange = "material_orange"
    airbnb = "airbnb"
    confetti = "confetti"


class FlatpickrOptions(BaseModel, extra=Extra.allow):
    """Flatpickr options to create flatpickr instance."""

    allowInput: Optional[bool]
    allowInvalidPreload: Optional[bool]
    altFormat: Optional[str]
    altInput: bool = True
    altInputClass: Optional[str]
    ariaDateFormat: Optional[str]
    clickOpens: Optional[bool]
    dateFormat: Optional[str]
    defaultDate: Optional[str]
    defaultHour: Optional[int] = Field(ge=0, le=23)
    defaultMinute: Optional[int] = Field(ge=0, le=59)
    disable: Optional[List[str]]
    disableMobile: Optional[bool]
    enable: Optional[List[str]]
    enableSeconds: Optional[bool]
    enableTime: Optional[bool]
    hourIncrement: Optional[int] = Field(ge=1, le=12)
    inline: Optional[bool]
    locale: Optional[str]
    maxDate: Optional[str]
    minDate: Optional[str]
    minuteIncrement: Optional[int] = Field(ge=0, le=59)
    mode: Optional[str]
    monthSelectorType: Optional[str]
    nextArrow: Optional[str]
    noCalendar: Optional[bool]
    position: Optional[str]
    prevArrow: Optional[str]
    shorthandCurrentMonth: Optional[bool]
    showMonths: Optional[int] = Field(ge=1, le=12)
    static: Optional[bool]
    time_24hr: Optional[bool]
    weekNumbers: Optional[bool]
    wrap: bool = True

    @validator("mode")
    def _disallow_mode(cls, v: str) -> NoReturn:
        raise ValueError(
            "Option mode is reserved and always set to static."
            " For range mode see how to use range picker in django-flatpickr docs"
        )

    @validator("dateFormat")
    def _disallow_dateFormat(cls, v: str) -> NoReturn:
        raise ValueError(
            "Option dateFormat is reserved and always set to Y-m-d."
            " Use altFormat to set date format selected by calendar"
        )

    @validator("altInput")
    def _disallow_altInput(cls, v: str) -> NoReturn:
        raise ValueError("Option altInput is reserved and always set to True.")

    @validator("wrap")
    def _disallow_wrap(cls, v: str) -> NoReturn:
        raise ValueError("Option wrap is reserved and always set to True.")

    @validator("enableTime")
    def _disallow_enableTime(cls, v: str) -> NoReturn:
        raise ValueError("Option enableTime is reserved and set based on widget used.")

    @validator("noCalendar")
    def _disallow_noCalendar(cls, v: str) -> NoReturn:
        raise ValueError("Option noCalendar is reserved and set based on widget used.")
