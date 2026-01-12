from tkinter.constants import CASCADE

from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total_area = models.FloatField(help_text="Общая площадь, м²")
    def __str__(self):
        return self.name

class Apartament(models.Model):
    number = models.CharField(max_length=255)
    building = models.ForeignKey(Building,on_delete=models.CASCADE,related_name="apartments")
    area = models.FloatField(help_text="Общая площадь, м²")
    residents_count = models.IntegerField(default=1) # Число жителей

    def __str__(self):
        return f"Квартира {self.number} ({self.building.name})"

class Meter(models.Model):
    serial_number = models.CharField(max_length=255) # Серийный номер
    apartament = models.ForeignKey(Apartament,on_delete=models.CASCADE,related_name="Счетчик")
    installation_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"Счетчик {self.serial_number}"

    def consuption_for_period(self,start_date,end_date):
        readings = self.readings.filter(date__gte=start_date,date__lte=end_date)

        if readings.count()<2:
            return 0

        first = readings.order_by('date').first().value
        last = readings.order_by('date').last().value

        return last - first

class MeterReading(models.Model):
    meter = models.ForeignKey(Meter,on_delete=models.CASCADE,related_name="Показания_счетчика")
    value = models.FloatField(help_text="Показание, кВт·ч")
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']
        unique_together = ('meter', 'date')

    def __str__(self):
        return f"{self.value} кВт·ч ({self.date})"