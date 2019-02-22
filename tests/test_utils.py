from django.test import SimpleTestCase

from django.views.generic.edit import CreateView
from flatpickr.utils import GenericViewWidgetMixin
from dev.myapp.models import Event


class CreateView(GenericViewWidgetMixin, CreateView):
    model = Event
    fields = []
    widgets = {}


class TestUtils(SimpleTestCase):

    def test_mixin(self):
        CreateView().get_form_class()
