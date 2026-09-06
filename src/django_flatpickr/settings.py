"""Package settings."""

import functools
from typing import Any

from django.conf import settings as django_settings
from pydantic import Field
from pydantic.fields import FieldInfo
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)

from .schemas import FlatpickrOptions, ThemeEnum


class _DjangoSettingsSource(PydanticBaseSettingsSource):
    """Settings source reading the `DJANGO_FLATPICKR` dict from Django settings."""

    def get_field_value(
        self, field: FieldInfo, field_name: str
    ) -> tuple[Any, str, bool]:
        return self().get(field_name), field_name, False

    def __call__(self) -> dict[str, Any]:
        return getattr(django_settings, "DJANGO_FLATPICKR", {})


class DjangoFlatpickrSettings(BaseSettings):
    """Package settings to customize inputs."""

    model_config = SettingsConfigDict(env_prefix="DJANGO_FLATPICKR_")

    theme_name: ThemeEnum | None = None
    theme_url: str | None = None
    template_name: str | None = None
    attrs: dict[str, str] = {}
    options: FlatpickrOptions = FlatpickrOptions()
    flatpickr_cdn_url: str = "https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/"
    app_static_url: str = (
        "https://cdn.jsdelivr.net/gh/monim67/django-flatpickr@2.0.0/src/django_flatpickr/static/django_flatpickr/"
    )
    debug: bool = Field(default_factory=lambda: getattr(django_settings, "DEBUG", True))

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """Add django settings as config source."""
        return (
            init_settings,
            env_settings,
            file_secret_settings,
            _DjangoSettingsSource(settings_cls),
        )


@functools.lru_cache(maxsize=1)
def get_django_flatpickr_settings() -> DjangoFlatpickrSettings:
    """Initialize and return DjangoFlatpickrSettings."""
    return DjangoFlatpickrSettings()
