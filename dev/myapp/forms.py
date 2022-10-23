from typing import Iterable

from django import forms
from django_filters import DateFilter, FilterSet

from dev.myapp.models import Event
from django_flatpickr.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    TimePickerInput,
)


class MyDatePickerInput(DatePickerInput):
    template_name = "myapp/custom-flatpickr-input.html"


class EventFilter(FilterSet):  # type: ignore
    start_date__gt = DateFilter(
        field_name="start_date",
        lookup_expr="gt",
        widget=MyDatePickerInput(),
    )
    start_date__lt = DateFilter(
        field_name="start_date",
        lookup_expr="lt",
        widget=MyDatePickerInput(range_from="start_date__gt"),
    )

    class Meta:
        model = Event
        fields: Iterable[str] = []


class ToDoForm(forms.Form):
    start_date = forms.DateField(label="Start Date", widget=DatePickerInput())
    end_date = forms.DateField(
        label="End Date", widget=DatePickerInput(range_from="start_date")
    )


class CustomInputTemplateToDoForm(forms.Form):
    start_date = forms.DateField(label="Start Date", widget=MyDatePickerInput())
    end_date = forms.DateField(
        label="End Date", widget=MyDatePickerInput(range_from="start_date")
    )


class EventForm(forms.ModelForm[Event]):
    class Meta:
        model = Event
        fields = [
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "start_datetime",
            "end_datetime",
        ]
        widgets = {
            "start_date": DatePickerInput(),
            "end_date": DatePickerInput(range_from="start_date"),
            "start_time": TimePickerInput(),
            "end_time": TimePickerInput(range_from="start_time"),
            "start_datetime": DateTimePickerInput(),
            "end_datetime": DateTimePickerInput(range_from="start_datetime"),
        }
