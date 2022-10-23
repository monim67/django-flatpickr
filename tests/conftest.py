"""Fixtures for tests."""

from typing import Iterable

import pytest
from pytest_django.fixtures import SettingsWrapper

from django_flatpickr.settings import get_django_flatpickr_settings


@pytest.fixture
def settings(settings: SettingsWrapper) -> Iterable[SettingsWrapper]:
    """Override pytest-django settings to clear get_django_flatpickr_settings cache."""
    get_django_flatpickr_settings.cache_clear()
    yield settings
    get_django_flatpickr_settings.cache_clear()
