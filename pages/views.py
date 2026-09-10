from django.contrib import messages
from django.shortcuts import redirect, render

from .emails import send_inquiry_email
from .forms import InquiryForm
from .models import ContactMessage, Service


def home(request):
    context = {
        'services': Service.objects.all()[:3],
    }
    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    context = {
        'services': Service.objects.all(),
    }
    return render(request, 'pages/services.html', context)


def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contact_message = ContactMessage.objects.create(
                business_name=data['business_name'],
                contact_name=data['contact_name'],
                email=data['email'],
                phone=data['phone'],
                is_operational=data['is_operational'],
                social_media_status=data['social_media_status'],
                social_media_links=data['social_media_links'],
                services_interested=', '.join(data['services_interested']),
                monthly_investment=data['monthly_investment'],
                referral_source=', '.join(data['referral_source']),
            )
            send_inquiry_email(contact_message)
            messages.success(
                request,
                "Thanks for reaching out — we'll get back to you within one business day.",
            )
            return redirect('pages:contact')
    else:
        form = InquiryForm()

    return render(request, 'pages/contact.html', {'form': form})
