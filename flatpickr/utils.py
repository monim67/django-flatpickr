from django.forms.models import modelform_factory


class GenericViewWidgetMixin:
    """
    Enables widgets property in django generic view classes.

    usage:
        class CreateView(GenericViewWidgetMixin, generic.edit.CreateView):
            model = MyModel
            fields = ['field1', 'field2']
            widgets = {
                'field1': widget1(),
                'field2': widget2(),
            }
    """
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields,
                                 widgets=self.widgets)
