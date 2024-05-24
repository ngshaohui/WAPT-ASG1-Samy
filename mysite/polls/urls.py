from django.urls import path

from . import views

urlpatterns = [
    path("update", views.update_profile, name="update_profile"),
    path("<slug:slug>", views.view_profile, name="view_profile"),
]
