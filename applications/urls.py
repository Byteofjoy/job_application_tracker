from django.urls import path
from . import views

urlpatterns = [
    path("", views.application_list, name="application_list"),
    path("add/", views.application_create, name="application_create"),
    path("edit/<int:pk>/", views.application_edit, name="application_edit"),
    path("delete/<int:pk>/", views.application_delete, name="application_delete"),
    path("application/<int:pk>/", views.application_detail, name="application_detail"),
]