# Customization

## Customize All Inputs

To customize the look and features of the flatpickr widget, copy the agent friendly settings block below to your
`settings.py` file and customize it. Settings apply globally to all flatpickr widgets used in your site.

```python
DJANGO_FLATPICKR = {
    # Name of the theme to use
    # More themes: https://flatpickr.js.org/themes/
    "theme_name": "dark",
    #
    # Complete URL of theme CSS file
    # theme_name is ignored if theme_url is provided
    # "theme_url": "https://..",
    #
    # Global HTML attributes for flatpickr <input> element
    # "attrs": {
    #     "class": "my-input-class",
    # },
    #
    # Global options for flatpickr
    # More options: https://flatpickr.js.org/options/
    # Some options are managed by this package and are reserved, see below.
    # "options": {
    #     "locale": "bn",             # locale option can be set here only
    #     "altFormat": "m/d/Y H:i",   # specify date format on the front-end
    # },
    #
    # HTML template to render the flatpickr input, see Template Customizing
    # "template_name": "your-app/custom-flatpickr-input.html",
    #
    # Specify CDN roots. Choose where static JS/CSS are served from.
    # Can be set to localhost (offline setup) or any other preferred CDN.
    # "flatpickr_cdn_url": "https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/",
    # "app_static_url": "https://cdn.jsdelivr.net/gh/monim67/django-flatpickr@2.0.0/src/django_flatpickr/static/django_flatpickr/",
    #
    # Advanced: To serve static files from Django's staticfiles instead of a CDN
    # (e.g. for GDPR / offline / compliance requirements), download the JS/CSS
    # files into a static directory, replace CDN links above with link to projects
    # static assets, and update app_static_url as below:
    # "app_static_url": "django_flatpickr/",
    # Note: you will be responsible for static file deployment in production
    # including collecting django static files and serving them from your web server.
}
```

## Customize Single Input

You should use options in `settings.py` to apply settings to all widget instances. If you need to
customize a single widget input, pass `attrs` and `options` directly to the widget instance.

```python
from django_flatpickr.schemas import FlatpickrOptions

class ToDoForm(forms.Form):
    todo = forms.CharField(widget=forms.TextInput())
    start_date = forms.DateField(widget=DatePickerInput(
        attrs={"class": "my-custom-class"}, # input element attributes
        options=FlatpickrOptions(altFormat="m/d/Y"),
    ))
```

### Reserved options

The following options are managed internally by the widget and will raise `ValueError` if set:

| Option       | Reason                                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `mode`       | Always set to `static`; range selection is implemented via `range_from` instead.                                            |
| `dateFormat` | Always fixed to the format needed to submit values back to Django; use `altFormat` to control the format shown to the user. |
| `altInput`   | Always `True`.                                                                                                              |
| `wrap`       | Always `True` (required for the input template's toggle/clear buttons).                                                     |
| `enableTime` | Set automatically based on the widget used (`TimePickerInput`/`DateTimePickerInput`).                                       |
| `noCalendar` | Set automatically based on the widget used (`TimePickerInput`).                                                             |

## JavaScript-only options and events

Some flatpickr options (and all event hooks, e.g. `onChange`) can only be set using JavaScript.

Set them globally for all widgets:

```javascript
window.djangoFlatpickrOptions = {
    onChange: function (selectedDates) { console.log(selectedDates) }
}
```

Or for a single widget, using the field's name:

```javascript
window.djangoFlatpickrOptions_start_date = {
    onChange: function (selectedDates) { console.log(selectedDates) }
}
```

!!! tip

    The field-specific key is derived from the field's `name` attribute with any formset prefix (e.g.
    `form-0-`) stripped, so `window.djangoFlatpickrOptions_start_date` applies to a `start_date` field
    regardless of which formset row it belongs to.

## Localization

Use the `locale` option, see [available localization options](https://flatpickr.js.org/localization/).
