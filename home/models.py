from django.db import models


class dpt(models.Model):
    department_name = models.CharField(max_length=200)
    dpt_discription = models.TextField(blank=True, default="")

    def __str__(self):
        return self.department_name


class doctor(models.Model):
    doctor_name=models.CharField(max_length=200)
    specilized=models.CharField(max_length=300)
    department_name=models.ForeignKey(dpt,on_delete=models.CASCADE)
    doctor_image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.doctor_name
    

class Booking(models.Model):
    pacient_name=models.CharField(max_length=200)
    pacient_phone_number=models.CharField(max_length=10)
    pacient_email=models.EmailField()
    doctor_name=models.ForeignKey(doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    def __str__(self):
        return f"{self.pacient_name} {self.doctor_name}"



class Contactinfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    message=models.TextField()
    address=models.TextField(blank=True)

    def __str__(self):
        return self.name