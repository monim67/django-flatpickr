"""Package settings."""
import functools
from typing import Any, Dict, Optional, Tuple

from django.conf import settings as django_settings

try:
    from pydantic.v1 import Field
    from pydantic.v1.env_settings import BaseSettings, SettingsSourceCallable
except ModuleNotFoundError:  # pragma: no cover
    from pydantic import Field  # type: ignore
    from pydantic.env_settings import (  # type: ignore
        BaseSettings,
        SettingsSourceCallable,
    )

from .schemas import FlatpickrOptions, ThemeEnum


def _django_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    return getattr(django_settings, "DJANGO_FLATPICKR", {})


class DjangoFlatpickrSettings(BaseSettings):
    """Package settings to customize inputs."""

    theme_name: Optional[ThemeEnum]
    theme_url: Optional[str]
    template_name: Optional[str]
    attrs: Dict[str, str] = {}
    options = FlatpickrOptions()
    flatpickr_cdn_url = "https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/"
    app_static_url = "https://cdn.jsdelivr.net/gh/monim67/django-flatpickr@2.0.0/src/django_flatpickr/static/django_flatpickr/"
    debug: bool = Field(default_factory=lambda: getattr(django_settings, "DEBUG", True))

    class Config:
        """Customize pydantic config."""

        env_prefix = "DJANGO_FLATPICKR_"

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> Tuple[SettingsSourceCallable, ...]:
            """Add django settings as config source."""
            return (
                init_settings,
                env_settings,
                file_secret_settings,
                _django_settings_source,
            )


@functools.lru_cache(maxsize=1)
def get_django_flatpickr_settings() -> DjangoFlatpickrSettings:
    """Initialize and return DjangoFlatpickrSettings."""
    return DjangoFlatpickrSettings()
