from django.test import SimpleTestCase

from flatpickr import DatePickerInput


class TestConfig(SimpleTestCase):

    def test_dateformat_override(self):
        widget = DatePickerInput(options={'dateFormat': 'my_format'})
        self.assertEqual(widget.config.options['altFormat'], 'my_format')
        self.assertEqual(
            widget.config.options['dateFormat'],
            DatePickerInput.option_overrides['dateFormat']
        )
