from django.contrib import admin
from .models import departments, doctors, bookings

# Register your models here.
admin.site.register(departments)
admin.site.register(doctors)
class Bookingadmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date','booked_on')
admin.site.register(bookings, Bookingadmin)