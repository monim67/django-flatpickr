django-flatpickr
================

This django widget contains Date-Picker, Time-Picker, DateTime-Picker input
widgets with date-range-picker functionality for django version >= 2.0.
The widget implements `flatpickr <https://github.com/flatpickr/flatpickr>`_
to display date-pickers in django model forms and custom forms which can be
configured easily for date-range selection. For Bootstrap date-picker see
`django-bootstrap-datepicker-plus <https://github.com/monim67/django-bootstrap-datepicker-plus>`_.


|  |ci-status| |coverage| |pyversions| |djversions|

|  |flatpickr-red-theme| |flatpickr-default-theme| |flatpickr-dark-theme|



Demo
----
-  `Custom Form <demo_custom_form_>`_.
-  `Model Form <demo_model_form_>`_.
-  `Generic View (without Model Form) <demo_generic_view_>`_.
-  `With django-crispy-forms <demo_crispy_form_>`_.
-  `With django-filter <demo_django_filter_>`_.
-  `With dynamic formsets <demo_dynamic_formset_>`_.



Getting Started
---------------


Prerequisites
^^^^^^^^^^^^^
-  Python >= 3.8
-  Django >= 2.0


Installing
^^^^^^^^^^
Install the PyPI package via pip.

::

    pip install django-flatpickr

Add ``django_flatpickr`` to ``INSTALLED_APPS`` in your ``settings.py`` file.

.. code:: python

    INSTALLED_APPS = [
        # Add the following
        "django_flatpickr",
    ]



Usage
-----

The HTML template must have the following to render the flatpickr widget.
A better example is `here <file_custom_form_html_>`_.

.. code:: html

    <!-- File: myapp/custom-form.html -->
    {{ form.media }}  {# Adds all flatpickr JS/CSS files from CDN #}
    {{ form.as_p }}   {# Renders the form #}

    <form method="post">
      {% csrf_token %}
      {% bootstrap_form form %}
    </form>


You can use it `with generic views without a model form <generic_view_block_>`_.
It can also be used with custom forms and model forms as below.


Usage in Custom Form
^^^^^^^^^^^^^^^^^^^^

.. code:: python

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


See `models.py <file_models_py_>`_, `forms.py <file_forms_py_>`_,
`views.py <file_views_py_>`_, `custom-form.html <file_custom_form_html_>`_
for more details.

Usage in Model Form
^^^^^^^^^^^^^^^^^^^^

.. code:: python

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


See `models.py <file_models_py_>`_, `forms.py <file_forms_py_>`_,
`views.py <file_views_py_>`_, `event_form.html <file_event_form_html_>`_
for more details.

Implement date-range-picker
^^^^^^^^^^^^^^^^^^^^^^^^^^^

DatePickers can be linked together to select a date-range, time-range or
date-time-range **without writing a single line of JavaScript**.

.. code:: python

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



Customization
-------------

To customize the look and features of flatpickr widget copy the
`settings block <settings_block_>`_ to your settings.py file and customize it.
Settings applies globally to all flatpickr widgets used in your site.

You can set date and event hook options using JavaScript.

.. code:: javascript

    window.djangoFlatpickrOptions = {
        onChange: function (selectedDates) { console.log(selectedDates) }
    }


Customize single input
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from django_flatpickr.schemas import FlatpickrOptions

    class ToDoForm(forms.Form):
        todo = forms.CharField(widget=forms.TextInput())
        start_date = forms.DateField(widget=DatePickerInput(
            attrs = {"class": "my-custom-class"}, # input element attributes
            options=FlatpickrOptions(altFormat="m/d/Y"),
        ))

Similarly set date and event hook options using JavaScript.

.. code:: javascript

    window.djangoFlatpickrOptions_start_date = {
        onChange: function (selectedDates) { console.log(selectedDates) }
    }


Localization
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use locale option, see `available localization options <https://flatpickr.js.org/localization/>`_.


License
-------

- `MIT LICENSE <https://github.com/monim67/django-flatpickr/blob/master/LICENSE>`_.
- `CONTRIBUTING <https://github.com/monim67/django-flatpickr/blob/master/.github/CONTRIBUTING.md>`_.
- `CODE_OF_CONDUCT <https://github.com/monim67/django-flatpickr/blob/master/.github/CODE_OF_CONDUCT.md>`_.


.. |flatpickr-red-theme| image:: https://cloud.githubusercontent.com/assets/11352152/14549374/3cc01102-028d-11e6-9ff4-0cf208a310c4.PNG
    :alt: Flatpickr Red Theme

.. |flatpickr-default-theme| image:: https://cloud.githubusercontent.com/assets/11352152/14549370/3cadb750-028d-11e6-818d-c6a1bc6349fc.PNG
    :alt: Flatpickr Default Theme

.. |flatpickr-dark-theme| image:: https://cloud.githubusercontent.com/assets/11352152/14549372/3cbc8514-028d-11e6-8daf-ec1ba01c9d7e.PNG
    :alt: Flatpickr Dark Theme


.. |ci-status| image:: https://github.com/monim67/django-flatpickr/actions/workflows/build.yml/badge.svg?event=push
    :target: https://github.com/monim67/django-flatpickr/actions/workflows/build.yml
    :alt: Build Status

.. |coverage| image:: https://coveralls.io/repos/github/monim67/django-flatpickr/badge.svg?branch=master
    :target: https://coveralls.io/github/monim67/django-flatpickr?branch=master
    :alt: Coverage Status

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/django-flatpickr.svg
    :target: https://pypi.python.org/pypi/django-flatpickr
    :alt: Python Versions

.. |djversions| image:: https://img.shields.io/pypi/djversions/django-flatpickr.svg
    :target: https://pypi.python.org/pypi/django-flatpickr
    :alt: DJango Versions



.. _demo_custom_form: https://monim67.github.io/django-flatpickr/demo/custom-form.html
.. _demo_model_form: https://monim67.github.io/django-flatpickr/demo/generic-view-with-model-form-1.html
.. _demo_generic_view: https://monim67.github.io/django-flatpickr/demo/generic-view.html
.. _demo_crispy_form: https://monim67.github.io/django-flatpickr/demo/crispy-form.html
.. _demo_django_filter: https://monim67.github.io/django-flatpickr/demo/django-filter.html
.. _demo_dynamic_formset: https://monim67.github.io/django-flatpickr/demo/dynamic-formset.html

.. _generic_view_block: https://github.com/monim67/django-flatpickr/blob/2.0.0/dev/myapp/views.py#L31
.. _settings_block: https://github.com/monim67/django-flatpickr/blob/2.0.0/dev/mysite/settings.py#L143-L200

.. _file_custom_form_html: https://github.com/monim67/django-flatpickr/blob/2.0.0/dev/myapp/templates/myapp/custom-form.html
.. _file_event_form_html: https://github.com/monim67/django-flatpickr/blob/2.0.0/dev/myapp/templates/myapp/event_form.html
.. _file_forms_py: https://github.com/monim67/django-flatpickr/blob/2.0.0/dev/myapp/forms.py
.. _file_views_py: https://github.com/monim67/django-flatpickr/blob/2.0.0/dev/myapp/views.py
.. _file_models_py: https://github.com/monim67/django-flatpickr/blob/2.0.0/dev/myapp/models.py
