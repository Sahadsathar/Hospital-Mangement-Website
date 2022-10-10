from django import forms
from . models import bookings

class Date_input(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = '__all__'
        widgets = { 'booking_date': Date_input()}
        labels = {
            'p_name' : "Patient Name: " ,
            'p_phone' : "Patient Phone number : " ,
            'p_email' : "Patient Email : " ,
            'doc_name' : "Doctor Name: " ,
            'booking_date' : "Booking Date : " ,
            }