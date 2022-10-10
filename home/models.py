from django.db import models

# Create your models here.
class departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    def __str__(self):
        return self.dep_name

class doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr' + self.doc_name + '-(' + self.doc_spec +')'

class bookings(models.Model):
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)