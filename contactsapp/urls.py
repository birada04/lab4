from django.urls import path
from . import views

urlpatterns = [
    path("contacts/", views.contacts, name="contacts"),
    path("groups/", views.contact_groups, name="contact_groups"),
    path("help/", views.help_page, name="help_page"),
]
