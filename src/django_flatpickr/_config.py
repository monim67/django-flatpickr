from typing import Any, Dict, Optional

try:
    from pydantic.v1 import BaseModel, Field
except ModuleNotFoundError:  # pragma: no cover
    from pydantic import BaseModel, Field  # type: ignore

from .schemas import FlatpickrOptions


class WidgetConfig(BaseModel):
    """Widget config which is passed to input on render."""

    picker_type: str
    options: FlatpickrOptions = Field(default_factory=FlatpickrOptions)
    range_from: Optional[str]

    def update_options(
        self,
        *options_args: Optional[FlatpickrOptions],
        overrides: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Update options merging FlatpickrOptions sequentially."""
        for options_arg in options_args:
            if options_arg is not None:
                self.options = self.options.copy(
                    update=options_arg.dict(exclude_unset=True)
                )
        if overrides is not None:
            self.options = self.options.copy(update=overrides)

    def to_attr_value(self) -> str:
        """Convert to attr string value."""
        return self.json(exclude_none=True)
