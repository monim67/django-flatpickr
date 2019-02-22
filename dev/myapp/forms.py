from django import forms
from .models import Event

from flatpickr import (
    DatePickerInput,
    TimePickerInput,
    DateTimePickerInput,
)


class ToDoForm(forms.Form):
    start_date = forms.DateField(
        label="Start Date",
        widget=DatePickerInput().start_of('custom event')
    )
    end_date = forms.DateField(
        label="End Date",
        widget=DatePickerInput().end_of('custom event')
    )
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'class': 'textarea'}))


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'start_date', 'end_date',
            'start_time', 'end_time',
            'start_datetime', 'end_datetime',
        ]
        widgets = {
            'start_date':     DatePickerInput().start_of('event active days'),
            'end_date':       DatePickerInput().end_of('event active days'),
            'start_time':     TimePickerInput().start_of('event active time'),
            'end_time':       TimePickerInput().end_of('event active time'),
            'start_datetime': DateTimePickerInput().start_of('event datetime'),
            'end_datetime':   DateTimePickerInput().end_of('event datetime'),
        }
