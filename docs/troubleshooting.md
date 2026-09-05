# Troubleshooting

If the date-picker calendar does not show up, check the following common causes.

## No errors anywhere, but the calendar does not show up

You forgot to add `{{ form.media }}` to your template. See [Configure template](getting-started.md#configure-template).

## Errors displayed in the browser console

!!! error "flatpickr js/css resources was not loaded, please check your CDN links"

    `{{ form.media }}` is missing, or the CDN it points to (`flatpickr_cdn_url`) is unreachable/blocked.
    See [Configure template](getting-started.md#configure-template).

!!! error "input must have a parent with class=\"django-flatpickr\""

    A custom input template (`template_name`) is missing the required `django-flatpickr` wrapper class. See
    [Template Customizing](template-customizing.md).

!!! error "range_from not found"

    The field name passed to `range_from=` does not match any rendered input's `name` attribute. If used
    inside a `django-filters` `FilterSet`, the name must match the **FilterSet field name**, see
    [Usage → django-filter quirk](usage.md#django-filter-range_from-uses-the-filterset-field-name).

!!! error "Multiple range_from found"

    More than one input on the page shares the `name` given to `range_from=`. Make sure field names are
    unique outside of Django's own formset-prefixing.

!!! error "range_from \"...\" is not a flatpickr input"

    The field referenced by `range_from` exists, but was not yet initialized as a flatpickr input when this
    field was processed. Inputs are wired up in document order, so make sure the `range_from` target field
    is rendered **before** the field that links to it. See
    [Usage → Implement date-range-picker](usage.md#implement-date-range-picker).

## Inline error banner on the page

If `DJANGO_FLATPICKR["debug"]` is `True` (the default follows Django's `DEBUG` setting), a failing input
shows an inline red error message next to it reading "Check browser console for errors...". Check the
browser console for the underlying error, then set `DEBUG=False` (or `DJANGO_FLATPICKR["debug"] = False`)
to hide this message in production.

## Fix 404 (Not Found) errors for JS/CSS assets

By default, flatpickr's JS/CSS and this package's JS are served from a CDN
(`flatpickr_cdn_url`/`app_static_url`), so 404s here are usually unrelated to Django's `collectstatic`.
If you have switched to self-hosting these files through Django's staticfiles (see the "Advanced" section
in [Customization](customization.md#customize-all-inputs)), make sure you have run:

```bash
python3 manage.py collectstatic
```

and that `STATIC_ROOT` is configured correctly in `settings.py`.

## My error is not listed here

Please [create an issue](https://github.com/monim67/django-flatpickr/issues/new/choose) on the project's
GitHub repository providing as much information as you can.
