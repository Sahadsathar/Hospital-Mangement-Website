# from django.http import HttpResponse
from django.shortcuts import render
from .models import departments, doctors as doctor2
from .forms import BookingForm
# Create your views here.
def index(request):
    person={
        'name': 'john',
        'age': 30,
        'place': 'calicut'
    }
    return render(request, "index.html", person)

def about(request):
    return render(request, "about.html")

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form= {
        'form': form
    }
    return render(request, "booking.html", dict_form)

def doctors(request):
    dict_docs = {
        'doctors': doctor2.objects.all()
    }
    return render(request, "doctors.html", dict_docs)

def contact(request):
    return render(request, "contact.html")

def department(request):
    dict_dept = {
        'dept': departments.objects.all()
    }
    return render(request, "department.html", dict_dept)