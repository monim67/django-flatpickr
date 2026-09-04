"""Fixtures for tests."""

from collections.abc import Iterable

import pytest
from pytest_django import Settings

from django_flatpickr.settings import get_django_flatpickr_settings


@pytest.fixture
def settings(settings: Settings) -> Iterable[Settings]:
    """Override pytest-django settings to clear get_django_flatpickr_settings cache."""
    get_django_flatpickr_settings.cache_clear()
    yield settings
    get_django_flatpickr_settings.cache_clear()
