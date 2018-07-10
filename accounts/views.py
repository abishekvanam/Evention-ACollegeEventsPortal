from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from crispy_forms.helper import FormHelper
from .models import UserProfile, User

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from %s from MYSITE.com' %(name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        message = '%s \n\n\n-%s\n %s' %(comment, name, emailFrom)
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
        title = "Thanks!"
        confirm_message = "We appreciate your feedback. We'll get back to you shortly."
        form = None
    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    return render(request, 'accounts/contact.html', context)

def events_redirect(request):
    return redirect('events:index')

def signup_redirect(request):
    return redirect('account_login')

def view_profile(request):
    userprofile = UserProfile.objects.all()
    return render(request, 'accounts/profile.html',{'userprofile':userprofile})
