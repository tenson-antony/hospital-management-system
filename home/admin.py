from django.contrib import admin
from .models import dpt
from .models import doctor
from .models import Booking,Contactinfo
# Register your models here.

admin.site.register(dpt)
admin.site.register(doctor)
admin.site.register(Booking)
admin.site.register(Contactinfo)