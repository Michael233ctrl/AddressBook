from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages

from .models import Contact
from .forms import ContactForm


class ContactList(ListView):
    model = Contact
    template_name = 'base/all-contacts.html'
    context_object_name = 'contacts'


def add_contact(request):
    action = 'add'
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
        else:
            messages.error(request, 'Invalid form')
    form = ContactForm()
    return render(request, 'base/contact.html', {'form': form, 'action': action})


def edit_contact(request, pk):
    action = 'edit'
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts')
        else:
            messages.error(request, 'Invalid form')
    form = ContactForm(instance=contact)
    return render(request, 'base/contact.html', {'form': form, 'action': action})
