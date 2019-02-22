from django.http import HttpResponseRedirect
from django.views import generic

from flatpickr import DateTimePickerInput, DatePickerInput, TimePickerInput
from flatpickr.utils import GenericViewWidgetMixin

from .models import Event
from .forms import ToDoForm, EventForm


class CreateView(GenericViewWidgetMixin, generic.edit.CreateView):
    model = Event
    fields = [
        'start_date', 'end_date',
        'start_time', 'end_time',
        'start_datetime', 'end_datetime',
    ]
    widgets = {
        'start_date':     DatePickerInput().start_of('event days'),
        'end_date':       DatePickerInput().end_of('event days'),
        'start_time':     TimePickerInput().start_of('event time'),
        'end_time':       TimePickerInput().end_of('event time'),
        'start_datetime': DateTimePickerInput().start_of('event dtime'),
        'end_datetime':   DateTimePickerInput().end_of('event dtime'),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_text'] = 'Generic View without using model form'
        context['submit_text'] = 'Create Event'
        return context


class UpdateView(generic.edit.UpdateView):
    model = Event
    form_class = EventForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_text'] = 'Generic View using model form'
        context['submit_text'] = 'Update Event'
        return context


class CustomFormView(generic.FormView):
    template_name = 'myapp/custom-form.html'
    form_class = ToDoForm

    def form_valid(self, form):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
