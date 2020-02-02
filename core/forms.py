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
            'mobile_no': forms.TextInput(attrs={'pattern':'[0-9]{10}'}),
            'pincode': forms.TextInput(attrs={'pattern': '[0-9]{6}'}),

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
        labels = {
            'preferred_joining_date': _('Preferred Joining Date (YYYY-MM-DD)'),
        }
        widgets = {
            # 'preferred_joining_date': forms.DateInput(),
            'contact_no': forms.TextInput(attrs={'pattern':'[0-9]{10}'}),
            'preferred_joining_date': forms.TextInput(attrs={'pattern': '[2][0][0-9]{2}-[0-9]{2}-[0-9]{2}'}),

        }

class BugReportForm(forms.ModelForm):
    class Meta:
        model = models.bug_report
        fields = '__all__'
        # labels =
        widgets = {
            'contact_no': forms.TextInput(attrs={'pattern':'[0-9]{10}'})
        }

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

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
