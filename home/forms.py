# 


from django import forms
from .models import Booking, Contactinfo

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["pacient_name", "pacient_phone_number", "pacient_email", "doctor_name", "booking_date"]
        labels = {
            "pacient_name": "pacient name",
            "pacient_phone_number": "phone number",
            "pacient_email": "email",
            "doctor_name": "doctor",
            "booking_date": "appoinment date"
        }
        widgets = {
            'pacient_name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'pacient_email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'pacient_phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-control'}),
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'doctor_name': forms.Select(attrs={'class': 'form-control'}),
        }


class ContactInfoForm(forms.Form):

    class meta:
        model = Contactinfo
        fields = ["name", "email", "phone_number", "message", "address"]
        labels = {
            "name": "name",
            "email": "email",
            "phone_number": "phone number",
            "message": "message",
            "address": "address"
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter your address', 'class': 'form-control'}),
        }
   