from django.db import models

class Cars(models.Model):
    TYPE = (
        ('1', 'hatch'),
        ('2', 'Sedan'),
        ('3', 'SUV'),
    )
    name = models.CharField(max_length=30, blank=False, null=False)
    model = models.CharField(max_length=1, choices=TYPE, blank=False, null=False, default='1')

    def __str__(self):
        return self.name

class Cliente(models.Model):
    name =  models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=30)
    car_model = models.ForeignKey(Cars, on_delete=models.CASCADE)

    def __str__(self):
        return self.name