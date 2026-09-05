# Getting Started

## Prerequisites

- Python >= 3.10
- Django >= 2.0

## Install

Install the PyPI package via pip.

```bash
pip install django-flatpickr
```

Add `django_flatpickr` to the list of `INSTALLED_APPS` in your `settings.py` file.

```python
INSTALLED_APPS = [
    # Add the following
    "django_flatpickr",
]
```

## Configure template

The widget requires `{{ form.media }}` in your template to load flatpickr's JS/CSS. The calendar will
silently not appear if `{{ form.media }}` is missing.

!!! tip

    For better page performance, use `{{ form.media.css }}` in `<head>` and `{{ form.media.js }}` just
    before `</body>`.

```html
<!-- File: myapp/custom-form.html -->
<!DOCTYPE html>
<html>
<head>
  {{ form.media }}
</head>
<body>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
</body>
</html>
```

Then head over to the [Usage](usage.md) page to see how to use it in forms and views.

## Quirks

### Formsets: use `formset.media`, not the media of individual forms

Django's `BaseFormSet` has its own `.media` property that aggregates widget assets across all its forms.
Use it once (outside the loop) rather than emitting media inside the loop for each form.

```html
{{ formset.media }}
{{ formset.management_form }}
{% for form in formset %}
  {{ form.as_p }}
{% endfor %}
```

See the [formset template in the demo app](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/templates/myapp/custom-formset.html).

### Dynamically added forms (modals, AJAX, dynamic formsets)

Unlike widgets that require re-initialization after new HTML is injected into the page, django-flatpickr
watches the whole document for changes and automatically initializes any flatpickr input that is added to
the DOM later — no extra JavaScript call is required on your end. This means forms shown in a modal
(rendered up-front and toggled with CSS, or injected later via AJAX), or new rows added by
[django-dynamic-formset](https://github.com/elo80ka/django-dynamic-formset), work out of the box as long as
`{{ form.media }}` (or `{{ formset.media }}`) has been rendered somewhere on the page at least once.

See the [modal demo template](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/templates/myapp/modal-window.html).
