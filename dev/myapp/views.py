from typing import Any

from django.forms import BaseForm, ModelForm, formset_factory
from django.forms.models import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django_filters.views import FilterView

from dev.myapp.forms import (
    CustomInputTemplateToDoForm,
    EventFilter,
    EventForm,
    ToDoForm,
)
from dev.myapp.models import Event
from django_flatpickr.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    TimePickerInput,
)


class AgentPromptMixin:
    """Adds a formatted agent_prompt to the template context for demo pages."""

    agent_prompt: str | None = None

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)  # type: ignore
        if self.agent_prompt:
            context["agent_prompt"] = self.agent_prompt.format(
                docs_url="https://monim67.github.io/django-flatpickr/llms.txt",
                repo_baseurl="https://github.com/monim67/django-flatpickr/blob/master",
            )
        return context


class EventListView(AgentPromptMixin, FilterView):  # type: ignore
    agent_prompt = """
- Docs: {docs_url}
- EventFilter (note range_from uses FilterSet field name): {repo_baseurl}/dev/myapp/forms.py
- EventListView: {repo_baseurl}/dev/myapp/views.py
- template: {repo_baseurl}/dev/myapp/templates/myapp/event_filter.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    filterset_class = EventFilter
    extra_context = {
        "title_text": "Generic View using model form",
        "submit_text": "Search",
        "lead_text": (
            "Shows how to use date picker widgets in a "
            '<a href="https://pypi.org/project/django-filter/">django-filter</a> FilterSet.'
        ),
    }


class CreateView(AgentPromptMixin, generic.edit.CreateView[Event, ModelForm[Event]]):
    agent_prompt = """
- Docs: {docs_url}
- CreateView (note get_form_class method): {repo_baseurl}/dev/myapp/views.py
- template (note how form.media is placed): {repo_baseurl}/dev/myapp/templates/myapp/event_form.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    model = Event
    fields = [
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "start_datetime",
        "end_datetime",
    ]
    extra_context = {
        "title_text": "Generic View without using model form",
        "submit_text": "Create Event",
        "lead_text": "Shows how to add date pickers to a generic CreateView by overriding get_form_class().",
    }

    def get_form_class(self) -> type[ModelForm[Event]]:
        return modelform_factory(
            self.model,
            fields=self.fields,
            widgets={
                "start_date": DatePickerInput(),
                "end_date": DatePickerInput(range_from="start_date"),
                "start_time": TimePickerInput(),
                "end_time": TimePickerInput(range_from="start_time"),
                "start_datetime": DateTimePickerInput(),
                "end_datetime": DateTimePickerInput(range_from="start_datetime"),
            },
        )


class UpdateView(AgentPromptMixin, generic.edit.UpdateView[Event, EventForm]):
    agent_prompt = """
- Docs: {docs_url}
- EventForm: {repo_baseurl}/dev/myapp/forms.py
- UpdateView: {repo_baseurl}/dev/myapp/views.py
- template (note how form.media is placed): {repo_baseurl}/dev/myapp/templates/myapp/event_form.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    model = Event
    form_class = EventForm
    extra_context = {
        "title_text": "Generic View using model form",
        "submit_text": "Update Event",
        "lead_text": "Shows how to add date pickers to a ModelForm using the Meta.widgets option.",
    }


class CustomFormView(AgentPromptMixin, generic.FormView[CustomInputTemplateToDoForm]):
    agent_prompt = """
- Docs: {docs_url}
- CustomInputTemplateToDoForm, MyDatePickerInput: {repo_baseurl}/dev/myapp/forms.py
- custom widget template: {repo_baseurl}/dev/myapp/templates/myapp/custom-flatpickr-input.html
- CustomFormView: {repo_baseurl}/dev/myapp/views.py
- template (note how form.media is placed): {repo_baseurl}/dev/myapp/templates/myapp/custom-form.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    template_name = "myapp/custom-form.html"
    form_class = CustomInputTemplateToDoForm
    extra_context = {
        "title_text": "Use customized input with addon clear button",
        "lead_text": "Shows how to use a custom input template with an addon clear button.",
    }

    def form_valid(self, form: BaseForm) -> HttpResponse:
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER", "/"))


class CrispyFormView(AgentPromptMixin, generic.FormView[ToDoForm]):
    agent_prompt = """
- Docs: {docs_url}
- ToDoForm: {repo_baseurl}/dev/myapp/forms.py
- CrispyFormView: {repo_baseurl}/dev/myapp/views.py
- template: {repo_baseurl}/dev/myapp/templates/myapp/crispy-form.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    template_name = "myapp/crispy-form.html"
    form_class = ToDoForm
    extra_context = {
        "title_text": "Use with django-crispy-forms",
        "lead_text": (
            "Shows how to use date pickers with "
            '<a href="https://pypi.org/project/django-crispy-forms/">django-crispy-forms</a>.'
        ),
    }

    def form_valid(self, form: BaseForm) -> HttpResponse:
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER", "/"))


class DynamicFormsetView(AgentPromptMixin, generic.FormView[ToDoForm]):
    agent_prompt = """
- Docs: {docs_url}
- DynamicFormsetView: {repo_baseurl}/dev/myapp/views.py
- template (note management_form and media outside loop): {repo_baseurl}/dev/myapp/templates/myapp/custom-formset.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    template_name = "myapp/custom-formset.html"
    form_class = formset_factory(ToDoForm, extra=2)  # type: ignore
    extra_context = {
        "title_text": "Use with Formsets",
        "lead_text": "Shows how to use date pickers in a Django formset.",
    }

    def form_valid(self, form: BaseForm) -> HttpResponse:
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER", "/"))


class ModalFormView(AgentPromptMixin, generic.edit.CreateView[Event, EventForm]):
    agent_prompt = """
- Docs: {docs_url}
- EventForm: {repo_baseurl}/dev/myapp/forms.py
- ModalFormView: {repo_baseurl}/dev/myapp/views.py
- template (note form.media is on parent page, not in modal): {repo_baseurl}/dev/myapp/templates/myapp/modal-window.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    model = Event
    form_class = EventForm
    template_name = "myapp/modal-window.html"
    extra_context = {
        "title_text": "Use in a Modal",
        "submit_text": "Submit",
        "lead_text": "Shows how to use date pickers in a modal window.",
    }
