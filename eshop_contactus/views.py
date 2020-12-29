from django.shortcuts import render

from .forms import contactUs_form
from .models import contactus_model

def contactUsPage(request):

    contactUs_form_del = contactUs_form(request.POST or None)
    context = {
        'contactus':contactUs_form_del
    }

    if contactUs_form_del.is_valid():

        username = contactUs_form_del.cleaned_data.get('username')
        email = contactUs_form_del.cleaned_data.get('email')
        subject = contactUs_form_del.cleaned_data.get('subject')
        msg = contactUs_form_del.cleaned_data.get('msg')

        contactus_model.objects.create(username=username, email=email, subject=subject, msg=msg)
        context['contactus'] = contactUs_form_del

    return render(request, 'contactus/contactUs.html', context)
