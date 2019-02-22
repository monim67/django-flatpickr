from django.test import SimpleTestCase

from flatpickr._base import BasePickerInput


class TestLinkedInputs(SimpleTestCase):

    def test_linking_inputs(self):
        BasePickerInput().start_of('an event')
        BasePickerInput().end_of('an event')
        self.assertTrue(True)  # all code above are working

    def test_error_on_unknown_linking(self):
        endpicker = BasePickerInput()
        self.assertRaises(KeyError, lambda: endpicker.end_of('unknown'))
