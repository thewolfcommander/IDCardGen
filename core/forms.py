from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User, StudentInformation, SchoolInformation

from .models import *

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    full_name = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    user_id = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    mobile_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('user_id', 'email', 'full_name', 'mobile_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.user_id = self.cleaned_data["user_id"]
        user.full_name = self.cleaned_data["full_name"]
        user.email = self.cleaned_data["email"]
        user.mobile_number = self.cleaned_data["mobile_number"]

        if commit:
            user.save()
        return user

class FeedbackForm(forms.ModelForm):
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput())
    message = forms.CharField(max_length=1055, required=True, widget=forms.Textarea())

    class Meta:
        model = Feedback
        fields = '__all__'

VERIFICATION_CHOICES = (
        ('True', 'True'),
        ('False', 'False'),
    )


class VerificationCardForm(forms.ModelForm):
    is_verified_by_student = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=VERIFICATION_CHOICES,)

    class Meta:
        model=VerificationCard
        fields = ('is_verified_by_student',)