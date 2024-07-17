from django.urls import path
from . import views

urlpatterns = [
    path("formPage/", views.form_name_view, name="Form name view"),
]