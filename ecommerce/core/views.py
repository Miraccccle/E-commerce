from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Setting, ContactForm, ContactMessage
# Create your views here.

def index(request):
    setting = Setting.objects.filter(status=True).first()
    context = {
        'setting': setting
    }
    return render(request, 'core/index.html', context)

def contact(request):
    setting = Setting.objects.filter(status=True).first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contactMessage = ContactMessage()
            contactMessage.name = form.cleaned_data['name']
            contactMessage.email = form.cleaned_data['email']
            contactMessage.subject = form.cleaned_data['subject']
            contactMessage.message = form.cleaned_data['message']
            contactMessage.ip = request.META.get('REMOTE_ADDR')
            contactMessage.save()
            messages.success(request, 'Message Send')

    form = ContactForm
    context = {
        'setting': setting,
        'form': form,
    }
    return render(request, 'core/contact.html', context)
