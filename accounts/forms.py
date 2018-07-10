from django.contrib.auth import get_user_model
from django import forms
from .models import User, UserProfile

ACCOUNT_TYPE = (
    ('part', 'Participant'),
    ('org', 'Organiser'),
    ('def', 'Default'),
)

class SignupForm(forms.ModelForm):
    # is_organizer = forms.BooleanField(required=False, label='Organiser Status')
    # is_participant = forms.BooleanField(required=False, label='Participant Status')
    user_type = forms.ChoiceField(choices = ACCOUNT_TYPE, label='Register as ')
    phone = forms.IntegerField(required=False, label='Phone Number')

    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','username','email','user_type','phone')

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user.userprofile.is_organizer = self.cleaned_data['is_organizer']
        # user.userprofile.is_participant = self.cleaned_data['is_participant']
        user.save()
        user.userprofile.user_type = self.cleaned_data['user_type']
        user.userprofile.phone = self.cleaned_data['phone']
        user.userprofile.save()

    # def __init__(self, *args, **kwargs):
    #     super(SignupForm, self).__init__(*args, **kwargs)
    #     self.fields['user_type'] = forms.ChoiceField(choices=ACCOUNT_TYPE)

class ContactForm(forms.Form):

    name = forms.CharField(required = True, max_length=120)
    email = forms.CharField(required = True)
    comment = forms.CharField(required = True, widget=forms.Textarea)
