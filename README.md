# django-flatpickr

This django widget contains Date-Picker, Time-Picker, DateTime-Picker
input widgets with date-range-picker functionality for django version
\>= 2.0. The widget implements [flatpickr](https://github.com/flatpickr/flatpickr) to display date-pickers in
django model forms and custom forms which can be configured easily for
date-range selection. For Bootstrap date-picker see
[django-bootstrap-datepicker-plus](https://github.com/monim67/django-bootstrap-datepicker-plus).

[![Build Status][ci-status]][ci-status-target] [![Coverage Status][coverage]][coverage-target]
[![Python Versions][pyversions]][pyversions-target] [![DJango Versions][djversions]][djversions-target]

![Flatpickr Red Theme][flatpickr-red-theme] ![Flatpickr Default Theme][flatpickr-default-theme]
![Flatpickr Dark Theme][flatpickr-dark-theme]

## Demo

- [Custom Form][demo_custom_form].
- [Model Form][demo_model_form].
- [Generic View (without Model Form)][demo_generic_view].
- [With django-crispy-forms][demo_crispy_form].
- [With django-filter][demo_django_filter].
- [With dynamic formsets][demo_dynamic_formset].
- [In a Modal Window][demo_modal_form].

## Getting Started

- Follow the [Getting Started documentation][doc_getting_started].
- Pass [llms.txt](https://monim67.github.io/django-flatpickr/llms.txt)/[llms-full.txt](https://monim67.github.io/django-flatpickr/llms-full.txt) to your coding agent.

## Usage

### Usage in Custom Form

```python
# File: forms.py
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from .models import Event
from django import forms

class ToDoForm(forms.Form):
    todo = forms.CharField(widget=forms.TextInput())
    date = forms.DateField(widget=DatePickerInput())
    time = forms.TimeField(widget=TimePickerInput())
    datetime = forms.DateTimeField(widget=DateTimePickerInput())
```

- [Usage in Model Form][doc_usage_model_form].
- [Usage in Generic View (without a Model Form)][doc_usage_generic_view].

### Implement date-range-picker

DatePickers can be linked together to select a date-range, time-range or
date-time-range **without writing a single line of JavaScript**.

```python
# File: forms.py
from django_flatpickr.widgets import DatePickerInput, TimePickerInput
from django import forms

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date", "end_date", "start_time", "end_time"]
        widgets = {
            "start_date": DatePickerInput(),
            "end_date": DatePickerInput(range_from="start_date"),
            "start_time": TimePickerInput(),
            "end_time": TimePickerInput(range_from="start_time"),
        }
```

- Read the full [Usage doc][doc_usage] for django-filter, django-crispy-forms, dynamic formsets and modal examples.

## Customization

- [Customize options, theme and localization][doc_customization].
- [Use a custom template for the widget input][doc_template_customizing].

## Contributing

- [CONTRIBUTING.md](https://github.com/monim67/django-flatpickr/blob/master/.github/CONTRIBUTING.md).
- [CODE_OF_CONDUCT.md](https://github.com/monim67/django-flatpickr/blob/master/.github/CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT LICENSE](https://github.com/monim67/django-flatpickr/blob/master/LICENSE).

[ci-status]: https://github.com/monim67/django-flatpickr/actions/workflows/build.yml/badge.svg?event=push
[ci-status-target]: https://github.com/monim67/django-flatpickr/actions/workflows/build.yml
[coverage]: https://coveralls.io/repos/github/monim67/django-flatpickr/badge.svg?branch=master
[coverage-target]: https://coveralls.io/github/monim67/django-flatpickr?branch=master
[demo_crispy_form]: https://monim67.github.io/django-flatpickr/demo/crispy-form.html
[demo_custom_form]: https://monim67.github.io/django-flatpickr/demo/custom-form.html
[demo_django_filter]: https://monim67.github.io/django-flatpickr/demo/django-filter.html
[demo_dynamic_formset]: https://monim67.github.io/django-flatpickr/demo/dynamic-formset.html
[demo_generic_view]: https://monim67.github.io/django-flatpickr/demo/generic-view.html
[demo_modal_form]: https://monim67.github.io/django-flatpickr/demo/modal-window.html
[demo_model_form]: https://monim67.github.io/django-flatpickr/demo/generic-view-with-model-form-1.html
[djversions]: https://img.shields.io/pypi/djversions/django-flatpickr.svg
[djversions-target]: https://pypi.python.org/pypi/django-flatpickr
[doc_customization]: https://monim67.github.io/django-flatpickr/customization/
[doc_getting_started]: https://monim67.github.io/django-flatpickr/getting-started/
[doc_template_customizing]: https://monim67.github.io/django-flatpickr/template-customizing/
[doc_usage]: https://monim67.github.io/django-flatpickr/usage/
[doc_usage_generic_view]: https://monim67.github.io/django-flatpickr/usage/#usage-in-generic-view-without-a-model-form
[doc_usage_model_form]: https://monim67.github.io/django-flatpickr/usage/#usage-in-model-form
[flatpickr-dark-theme]: https://cloud.githubusercontent.com/assets/11352152/14549372/3cbc8514-028d-11e6-8daf-ec1ba01c9d7e.PNG
[flatpickr-default-theme]: https://cloud.githubusercontent.com/assets/11352152/14549370/3cadb750-028d-11e6-818d-c6a1bc6349fc.PNG
[flatpickr-red-theme]: https://cloud.githubusercontent.com/assets/11352152/14549374/3cc01102-028d-11e6-9ff4-0cf208a310c4.PNG
[pyversions]: https://img.shields.io/pypi/pyversions/django-flatpickr.svg
[pyversions-target]: https://pypi.python.org/pypi/django-flatpickr
