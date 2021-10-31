from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages

from .models import Contact
from .forms import AddContactForm


class ContactList(ListView):
    model = Contact
    template_name = 'base/all-contacts.html'
    context_object_name = 'contacts'


def add_contact(request):
    if request.method == 'POST':
        form = AddContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
        else:
            messages.error(request, 'Invalid form')
    form = AddContactForm()
    return render(request, 'base/add-contact.html', {'form': form})


