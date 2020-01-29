from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models


class LibraryForm(forms.ModelForm):
    class Meta:
        model = models.library
        exclude = ['owner', 'verified','visible','views']
        # fields = '__all__'
        # labels =
        # widgets =
        widgets = {
            'opening_time': forms.TimeInput(),
            'closing_time': forms.TimeInput(),
            'ammenities': forms.SelectMultiple(),
            'payment_methods': forms.SelectMultiple(),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name']
        # labels =
        # widgets =

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = models.enquiry
        fields = '__all__'
        # labels =
        # widgets =

class BugReportForm(forms.ModelForm):
    class Meta:
        model = models.bug_report
        fields = '__all__'
        # labels =
        # widgets =

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = models.testimonial
        fields = '__all__'
        # labels =
        # widgets =

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = models.newsletter
        fields = '__all__'