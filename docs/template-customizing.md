# Template Customizing

The calendar itself is not customizable via templates, but the input field's wrapper markup can be. Create
an HTML template for the widget input:

```html
<!-- File: myapp/templates/myapp/custom-flatpickr-input.html -->
<div class="django-flatpickr field has-addons">
  <!-- The root element must have the "django-flatpickr" class -->

  <div class="control is-expanded">
    {% include 'django/forms/widgets/text.html' %}
    <!-- It generates the HTML <input> element -->
  </div>

  <div class="control">
    <button type="button" class="button" data-toggle>
      <!-- Optional calendar-toggle button, must have the data-toggle attribute -->
      Open
    </button>
  </div>

  <div class="control">
    <button type="button" class="button" data-clear>
      <!-- Optional clear button, must have the data-clear attribute -->
      Clear
    </button>
  </div>
</div>
```

!!! note

    The `django-flatpickr` wrapper class and the `{% include 'django/forms/widgets/text.html' %}` input are
    required. The `data-toggle`/`data-clear` buttons are optional and are flatpickr's native
    [`wrap` mode](https://flatpickr.js.org/examples/#wrapping-in-custom-elements-eg-input-groups) convention,
    which this package always enables.

See the [full working example in the demo app](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/templates/myapp/custom-flatpickr-input.html).

## Apply globally

Add it to the `DJANGO_FLATPICKR` settings to use it for every widget in your site.

```python
DJANGO_FLATPICKR = {
    "template_name": "myapp/custom-flatpickr-input.html",
}
```

## Apply to a single widget

Subclass the widget and override `template_name` to use the custom template for just that widget.

```python
from django_flatpickr.widgets import DatePickerInput

class MyDatePickerInput(DatePickerInput):
    template_name = "myapp/custom-flatpickr-input.html"
```

See [forms.py](https://github.com/monim67/django-flatpickr/blob/master/dev/myapp/forms.py) (`MyDatePickerInput`)
for the full working example.
