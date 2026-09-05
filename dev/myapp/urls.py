from django.urls import path

from dev.myapp import views

from .utils import http_meta_redirect_view

app_name = "myapp"

urlpatterns = [
    path(
        "",
        http_meta_redirect_view("generic-view-with-model-form-1.html"),
    ),
    path("generic-view.html", views.CreateView.as_view(), name="generic-view"),
    path(
        "generic-view-with-model-form-<int:pk>.html",
        views.UpdateView.as_view(),
        name="model-form",
    ),
    path("custom-form.html", views.CustomFormView.as_view(), name="custom-form"),
    path("crispy-form.html", views.CrispyFormView.as_view(), name="crispy-form"),
    path("django-filter.html", views.EventListView.as_view(), name="django-filter"),
    path(
        "dynamic-formset.html",
        views.DynamicFormsetView.as_view(),
        name="dynamic-formset",
    ),
    path("modal-window.html", views.ModalFormView.as_view(), name="modal-window"),
]
