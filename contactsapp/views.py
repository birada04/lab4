from django.shortcuts import render
from .models import Contact, ContactGroup


def contacts(request):
    contact_list = Contact.objects.order_by("first_name")
    contact_dict = {"contacts": contact_list}
    return render(request, "contacts.html", context=contact_dict)


def contact_groups(request):
    group_list = ContactGroup.objects.all()
    group_dict = {"groups": group_list}
    return render(request, "groups.html", context=group_dict)


def help_page(request):
    return render(request, "help.html")
