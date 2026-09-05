# Usage

## Usage in Custom Form

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


# File: views.py
class CustomFormView(generic.FormView):
    template_name = "myapp/custom-form.html"
    form_class = ToDoForm
```

See [forms.py](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/forms.py),
[views.py](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/views.py) for more details.

## Usage in Model Form

```python
# File: forms.py
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from .models import Event
from django import forms

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "start_date", "start_time", "start_datetime"]
        widgets = {
            "start_date": DatePickerInput(),
            "start_time": TimePickerInput(),
            "start_datetime": DateTimePickerInput(),
        }


# File: views.py
class UpdateView(generic.edit.UpdateView):
    model = Event
    form_class = EventForm
```

## Usage in Generic View (without a Model Form)

Override `get_form_class()` with `modelform_factory` to attach the widgets without declaring a dedicated
`ModelForm` class.

```python
# File: views.py
from django.forms.models import modelform_factory
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class CreateView(generic.edit.CreateView):
    model = Event
    fields = ["start_date", "start_time", "start_datetime"]

    def get_form_class(self):
        return modelform_factory(
            self.model,
            fields=self.fields,
            widgets={
                "start_date": DatePickerInput(),
                "start_time": TimePickerInput(),
                "start_datetime": DateTimePickerInput(),
            },
        )
```

See [views.py](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/views.py) `CreateView` for
the full working example.

## Types of DatePickers

- `DatePickerInput` — Date-Picker Calendar.
- `TimePickerInput` — Time-Picker Calendar.
- `DateTimePickerInput` — DateTime-Picker Calendar.

## Implement date-range-picker

DatePickers can be linked together to select a date-range, time-range or date-time-range **without
writing a single line of JavaScript**.

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

!!! important

    The field referenced by `range_from` must be rendered **before** the field that links to it in the
    template/HTML output. Inputs are wired up in document order on page load, so if the linked field
    appears earlier than its `range_from` target, the browser console will show
    `range_from "..." is not a flatpickr input`. See [Troubleshooting](troubleshooting.md) for details.

## Quirks

### django-filter: `range_from` uses the FilterSet field name

When using `DatePickerInput` inside a `django-filters` `FilterSet`, pass the **FilterSet field name** to
`range_from` — not the underlying model field name.

```python
from django_filters import DateFilter, FilterSet
from django_flatpickr.widgets import DatePickerInput

class EventFilter(FilterSet):
    start_date__gt = DateFilter(
        field_name="start_date",
        lookup_expr="gt",
        widget=DatePickerInput(),
    )
    start_date__lt = DateFilter(
        field_name="start_date",
        lookup_expr="lt",
        widget=DatePickerInput(range_from="start_date__gt"),  # FilterSet field name, not model field name
    )
```

See the [full working example in the demo app](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/forms.py) (`EventFilter`).

### django-crispy-forms

Both rendering styles work with `{{ form.media }}` already on the page:

```html
{% load crispy_forms_tags %}
{{ form.media }}

<!-- Using {% crispy form %} -->
<form method="post">
  {% csrf_token %}
  {% crispy form %}
</form>

<!-- Using the |crispy filter -->
<form method="post">
  {% csrf_token %}
  {{ form | crispy }}
</form>
```

See the [crispy-form.html demo template](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/templates/myapp/crispy-form.html).

### Dynamic formsets

Combine with [elo80ka/django-dynamic-formset](https://github.com/elo80ka/django-dynamic-formset) to let
users add/remove rows on the client; newly added rows are automatically picked up (see
[Getting Started → Dynamically added forms](getting-started.md#dynamically-added-forms-modals-ajax-dynamic-formsets)).

```html
{{ formset.media }}
<form method="post">
  {% csrf_token %}
  {{ formset.management_form }}
  {% for form in formset %}
  <div class="formset">{{ form }}</div>
  {% endfor %}
</form>
<script src="https://code.jquery.com/jquery-3.6.1.min.js"></script>
<script src="https://cdn.jsdelivr.net/gh/elo80ka/django-dynamic-formset@v1.2.2/src/jquery.formset.js"></script>
<script>
  $(".formset").formset();
</script>
```

See the [custom-formset.html demo template](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/templates/myapp/custom-formset.html).
