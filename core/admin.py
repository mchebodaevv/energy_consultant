from django.contrib import admin
from .models import Building, Apartament, Meter, MeterReading
# Register your models here.
admin.site.register(Building)
admin.site.register(Apartament)
admin.site.register(Meter)
admin.site.register(MeterReading)