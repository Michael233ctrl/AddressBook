from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages

from .models import Contact
from .forms import ContactForm


class ContactList(ListView):
    model = Contact
    template_name = 'base/contacts.html'
    context_object_name = 'contacts'


def contact_list(request):
    contact = Contact.objects.all()
    return render(request, 'base/contacts.html', {'contacts': contact})


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


def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts')
    return render(request, 'base/delete.html', {'item': contact})


def search_contact(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        contact = Contact.objects.filter(
            Q(first_name__contains=searched) | Q(last_name__contains=searched) | Q(address__contains=searched) |
            Q(city__contains=searched) | Q(country__contains=searched) | Q(phone_number__contains=searched)
        )

        return render(request, 'base/search.html', {'searched': searched, 'contacts': contact})

    return render(request, 'base/search.html', {})
