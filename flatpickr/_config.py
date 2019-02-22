from flatpickr._helpers import JSONSerializable
from flatpickr._settings import WidgetSettings


class WidgetConfig(JSONSerializable):
    """Keeps track of all date-picker input classes."""

    id = None
    picker_type = None
    linked_to = None
    options = None
    _json_keys = ['id', 'picker_type', 'linked_to', 'options']

    _index = 0
    events = dict()

    @classmethod
    def generate_id(cls):
        """Return a unique ID for each date-picker input class."""
        cls._index += 1
        return 'fp_%s' % cls._index

    def __init__(self, picker_type):
        self.id = self.__class__.generate_id()
        self.picker_type = picker_type

    def _calculate_options(self, options, option_overrides):
        """Calculate and Return the options."""
        _options = {}
        _options.update(WidgetSettings.OPTIONS)
        _options.update(options if isinstance(options, dict) else {})
        if 'dateFormat' in _options and 'altFormat' not in _options:
            _options['altFormat'] = _options.pop('dateFormat')
        _options.update(option_overrides)
        self.options = _options
