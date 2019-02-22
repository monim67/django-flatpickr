from flatpickr._helpers import load_settings


@load_settings('FLATPICKR_SETTINGS')
class WidgetSettings:
    """ Settings can be overriden by FLATPICKR_SETTINGS in settings.py."""

    THEME_NAME = None
    THEME_URL = None
    TEMPLATE_NAME = None
    ATTRS = {}
    OPTIONS = {}
    NPM_URL = 'https://cdn.jsdelivr.net/npm/'
    GITHUB_URL = 'https://cdn.jsdelivr.net/gh/'
