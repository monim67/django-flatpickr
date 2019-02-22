from django.test import SimpleTestCase

from flatpickr import DatePickerInput


class TestContextRender(SimpleTestCase):

    def test_get_context(self):
        dp_input = DatePickerInput()
        context = dp_input.get_context('input_name', '2018-04-12', {})
        self.assertEqual(context['widget']['name'], 'input_name')
        self.assertEqual(context['widget']['value'], '2018-04-12')
        self.assertEqual(
            context['widget']['attrs']['fp_config'],
            dp_input.config.to_json()
        )

    def test_date_input_snapshot(self):
        dp_input = DatePickerInput()
        html = dp_input.render('input_name', '2018-04-12', {})
        self.assertTrue(html)
