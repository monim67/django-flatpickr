# django-flatpickr Project Overview

## What this project is

Django form widget library providing `DatePickerInput`, `TimePickerInput`, `DateTimePickerInput`. Wraps the
[flatpickr](https://github.com/flatpickr/flatpickr) JS library (not Bootstrap) with built-in
date-range-picker linking (`range_from`). Sister project
[django-bootstrap-datepicker-plus](https://github.com/monim67/django-bootstrap-datepicker-plus) is the
Bootstrap equivalent — don't port Bootstrap-specific concepts (jQuery, Month/Year pickers, etc.) here.

## Package layout (`src/django_flatpickr/`)

- `widgets.py` — public widgets (`DatePickerInput`, `TimePickerInput`, `DateTimePickerInput`).
- `_base.py` — `BasePickerInput`, shared widget logic (private, leading underscore).
- `schemas.py` — pydantic models: `FlatpickrOptions` (user-facing, some options reserved/validated), `ThemeEnum`.
- `settings.py` — `DjangoFlatpickrSettings`, reads the `DJANGO_FLATPICKR` dict from Django settings.
- `_media.py` — builds JS/CSS `Media` file lists (CDN by default).
- `static/django_flatpickr/js/django-flatpickr.js` — runtime JS: initializes flatpickr on `[data-fpconfig]`
  inputs, watches the DOM via `MutationObserver`, wires up `range_from` linking (fields must be in DOM order:
  the `range_from` target must render before the field linking to it).
- `templates/django_flatpickr/input.html` — default input template; custom templates must keep the
  `django-flatpickr` wrapper class.
- Supports pydantic v1 and v2 via a `try: from pydantic.v1 import ... except ModuleNotFoundError: from
  pydantic import ...` shim — preserve this pattern when touching `schemas.py`/`settings.py`.

## Dev/demo app

- `dev/` is a full Django project (`dev/mysite` settings, `dev/myapp` demo app) used for local development
  and to power the live demo site. Run with `poetry run poe start`.
- `dev/myapp/forms.py`/`views.py`/`templates/` demonstrate real usage (custom form, model form, generic view
  via `modelform_factory`, django-filter, django-crispy-forms, dynamic formsets, modal). Treat these as the
  source of truth for docs/examples — don't invent unverified usage patterns.

## Tests & tooling

- `tests/` — pytest + pytest-django, run via `poetry run poe test-cov`.
- Poetry (`pyproject.toml`) + poethepoet tasks: `poe start`, `poe lint`, `poe test-cov`.
- `tox` runs tests across Python 3.10–3.14. Supports Django `>=2,<6`, Python `>=3.10,<4`.

## Docs

- `docs/*.md` + `mkdocs.yml` — mkdocs site (readthedocs theme, explicit `nav`). Built output goes to
  `pages/` (gitignored, no CI build step — run `mkdocs build` or `mkdocs serve` manually to verify).
- `README.md` is the canonical readme. `pyproject.toml`'s `poe lint` still runs `rstcheck README.rst`, a
  stale reference from before the RST→Markdown migration.

## Formatting

Formatting (black, isort) is handled by the editor's format-on-save — never manually reformat code or "fix"
formatting; it's not the agent's concern.
