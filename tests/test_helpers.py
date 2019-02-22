from django.test import SimpleTestCase

from flatpickr._helpers import JSONSerializer


class TestHelpers(SimpleTestCase):

    def test_serializer(self):
        self.assertEqual(JSONSerializer().encode(1), '1')
