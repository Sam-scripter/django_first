from django.urls import path
from . import views

app_name = "template_app"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("other/", views.other, name="other"),
    path("base/", views.base, name="base"),
    path("relative/", views.relative, name="relative")
]