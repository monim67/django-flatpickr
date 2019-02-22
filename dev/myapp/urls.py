from django.urls import path

from . import views
from meta_redirect.views import MetaRedirectView

app_name = 'myapp'

urlpatterns = [
     path('', MetaRedirectView.as_view(redirect_url='generic-view.html')),
     path('generic-view.html',
          views.CreateView.as_view(), name='generic-view'),
     path('generic-view-with-model-form-<int:pk>.html',
          views.UpdateView.as_view(), name='model-form'),
     path('custom-form.html',
          views.CustomFormView.as_view(), name='custom-form'),
]
