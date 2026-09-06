from typing import Any

from pydantic import BaseModel, Field

from .schemas import FlatpickrOptions


class WidgetConfig(BaseModel):
    """Widget config which is passed to input on render."""

    picker_type: str
    options: FlatpickrOptions = Field(default_factory=FlatpickrOptions)
    range_from: str | None = None

    def update_options(
        self,
        *options_args: FlatpickrOptions | None,
        overrides: dict[str, Any] | None = None,
    ) -> None:
        """Update options merging FlatpickrOptions sequentially."""
        for options_arg in options_args:
            if options_arg is not None:
                self.options = self.options.model_copy(
                    update=options_arg.model_dump(exclude_unset=True)
                )
        if overrides is not None:
            self.options = self.options.model_copy(update=overrides)

    def to_attr_value(self) -> str:
        """Convert to attr string value."""
        return self.model_dump_json(exclude_none=True)
