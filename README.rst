django-flatpickr
================

This django widget contains Date-Picker, Time-Picker, DateTime-Picker input
widgets with date-range-picker functionality for django version >= 2.0.
The widget implements `flatpickr <https://github.com/flatpickr/flatpickr>`_
to display date-pickers in django model forms and custom forms which can be
configured easily for date-range selection. For Bootstrap date-picker see
`django-bootstrap-datepicker-plus <https://github.com/monim67/django-bootstrap-datepicker-plus>`_.


|  |flatpickr-red-theme| |flatpickr-default-theme| |flatpickr-dark-theme|



Demo
----
-  `Custom Form <demo_custom_form_>`_.
-  `Model Form <demo_model_form_>`_.
-  `Generic View (without Model Form) <demo_generic_view_>`_.



Getting Started
---------------


Prerequisites
^^^^^^^^^^^^^
-  Python >= 3.4
-  Django >= 2.0


Installing
^^^^^^^^^^
Install the PyPI package via pip.

::

    pip install django-flatpickr

Add ``flatpickr`` to ``INSTALLED_APPS`` in your ``settings.py`` file.

.. code:: python

    INSTALLED_APPS = [
        # Add the following
        'flatpickr',
    ]



Usage
-----

The HTML template must have the following to render the flatpickr widget.
A better example is `here <file_custom_form_html_>`_.

.. code:: html

    <!-- File: todo.html -->
    {{ form.media }}  {# Adds all flatpickr JS/CSS files from CDN #}
    {{ form.as_p }}   {# Renders the form #}


You can use it `with generic views without a model form <generic_view_block_>`_.
It can also be used with custom forms and model forms as below.


Usage in Custom Form
^^^^^^^^^^^^^^^^^^^^

.. code:: python

    # File: forms.py
    from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
    from .models import Event
    from django import forms

    class ToDoForm(forms.Form):
        todo = forms.CharField(widget=forms.TextInput())
        date = forms.DateField(widget=DatePickerInput())
        time = forms.TimeField(widget=TimePickerInput())
        datetime = forms.DateTimeField(widget=DateTimePickerInput())


    # File: views.py
    class CustomFormView(generic.FormView):
        template_name = 'myapp/custom-form.html'
        form_class = ToDoForm


See `models.py <file_models_py_>`_, `forms.py <file_forms_py_>`_,
`views.py <file_views_py_>`_, `custom-form.html <file_custom_form_html_>`_
for more details.

Usage in Model Form
^^^^^^^^^^^^^^^^^^^^

.. code:: python

    # File: forms.py
    from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
    from .models import Event
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'start_date', 'start_time', 'start_datetime']
            widgets = {
                'start_date': DatePickerInput(),
                'start_time': TimePickerInput(),
                'start_datetime': DateTimePickerInput(),
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
    from flatpickr import DatePickerInput, TimePickerInput
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'start_date', 'end_date', 'start_time', 'end_time']
            widgets = {
                'start_date':DatePickerInput().start_of('event days'),
                'end_date':DatePickerInput().end_of('event days'),
                'start_time':TimePickerInput().start_of('party time'),
                'end_time':TimePickerInput().end_of('party time'),
            }



Customization
-------------

To customize the look and features of flatpickr widget copy the
`settings block <settings_block_>`_ to your settings.py file and customize it.
Settings applies globally to all flatpickr widgets used in your site.

If you need to customize a single flatpickr widget you can do it as follows:

.. code:: python

    class ToDoForm(forms.Form):
        todo = forms.CharField(widget=forms.TextInput())
        date = forms.DateField(widget=DatePickerInput(
            attrs = {    # input element attributes
                "class": "my-custom-class",
            },
            options = {  # flatpickr options
                "dateFormat": "m/d/Y",
            }
        ))



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


.. _demo_custom_form: https://monim67.github.io/django-flatpickr/demo/custom-form.html
.. _demo_model_form: https://monim67.github.io/django-flatpickr/demo/generic-view-with-model-form-1.html
.. _demo_generic_view: https://monim67.github.io/django-flatpickr/demo/generic-view.html

.. _generic_view_block: https://github.com/monim67/django-flatpickr/blob/v1.0.0/dev/myapp/views.py#L11
.. _settings_block: https://github.com/monim67/django-flatpickr/blob/v1.0.0/dev/mysite/settings.py#L134-L176

.. _file_custom_form_html: https://github.com/monim67/django-flatpickr/blob/v1.0.0/dev/myapp/templates/myapp/custom-form.html
.. _file_event_form_html: https://github.com/monim67/django-flatpickr/blob/v1.0.0/dev/myapp/templates/myapp/event_form.html
.. _file_forms_py: https://github.com/monim67/django-flatpickr/blob/v1.0.0/dev/myapp/forms.py
.. _file_views_py: https://github.com/monim67/django-flatpickr/blob/v1.0.0/dev/myapp/views.py
.. _file_models_py: https://github.com/monim67/django-flatpickr/blob/v1.0.0/dev/myapp/models.py

