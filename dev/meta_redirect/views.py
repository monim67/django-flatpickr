from django.views.generic import TemplateView


class MetaRedirectView(TemplateView):
    redirect_url = '/'
    template_name = "meta_redirect/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['redirect_url'] = self.redirect_url
        return context
