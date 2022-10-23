from typing import Type

from django.forms import BaseForm, ModelForm, formset_factory
from django.forms.models import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django_filters.views import FilterView

from dev.myapp.forms import (
    CustomInputTemplateToDoForm,
    EventFilter,
    EventForm,
    ToDoForm,
)
from dev.myapp.models import Event
from django_flatpickr.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    TimePickerInput,
)


class EventListView(FilterView):  # type: ignore
    filterset_class = EventFilter
    extra_context = {
        "title_text": "Generic View using model form",
        "submit_text": "Search",
    }


class CreateView(generic.edit.CreateView[Event, ModelForm[Event]]):
    model = Event
    fields = [
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "start_datetime",
        "end_datetime",
    ]
    extra_context = {
        "title_text": "Generic View without using model form",
        "submit_text": "Create Event",
    }

    def get_form_class(self) -> Type[ModelForm[Event]]:
        return modelform_factory(
            self.model,
            fields=self.fields,
            widgets={
                "start_date": DatePickerInput(),
                "end_date": DatePickerInput(range_from="start_date"),
                "start_time": TimePickerInput(),
                "end_time": TimePickerInput(range_from="start_time"),
                "start_datetime": DateTimePickerInput(),
                "end_datetime": DateTimePickerInput(range_from="start_datetime"),
            },
        )


class UpdateView(generic.edit.UpdateView[Event, EventForm]):
    model = Event
    form_class = EventForm
    extra_context = {
        "title_text": "Generic View using model form",
        "submit_text": "Update Event",
    }


class CustomFormView(generic.FormView[CustomInputTemplateToDoForm]):
    template_name = "myapp/custom-form.html"
    form_class = CustomInputTemplateToDoForm
    extra_context = {
        "title_text": "Use customized input with addon clear button",
    }

    def form_valid(self, form: BaseForm) -> HttpResponse:
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER", "/"))


class CrispyFormView(generic.FormView[ToDoForm]):
    template_name = "myapp/crispy-form.html"
    form_class = ToDoForm
    extra_context = {
        "title_text": "Use with django-crispy-forms",
    }

    def form_valid(self, form: BaseForm) -> HttpResponse:
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER", "/"))


class DynamicFormsetView(generic.FormView[ToDoForm]):
    template_name = "myapp/custom-formset.html"
    form_class = formset_factory(ToDoForm, extra=2)  # type: ignore
    extra_context = {
        "title_text": "Use with Formsets",
    }

    def form_valid(self, form: BaseForm) -> HttpResponse:
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER", "/"))
