from django.urls import path
from . import views


urlpatterns = [
    path("startPage/", views.index, name='index')
]