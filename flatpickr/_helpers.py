"""Contains the helper classes and methods used throughout the project."""

from json import JSONEncoder


class JSONSerializer(JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '_json_keys'):
            return {k: getattr(obj, k, None) for k in obj._json_keys}
        # else:
        #     return super().default(obj)


class JSONSerializable(JSONEncoder):
    def to_json(self):
        return JSONSerializer().encode(self)


def load_settings(settings_group_name):
    """Load settings from settings.py and override defaults."""
    def inner(_class):
        from django.conf import settings
        if hasattr(settings, settings_group_name):
            settings_dict = getattr(settings, settings_group_name)
            if isinstance(settings_dict, dict):
                for key, value in settings_dict.items():
                    setattr(_class, key.upper(), value)
        return _class
    return inner
