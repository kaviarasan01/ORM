from django.db import models

# Create your models here.
class Car(models.Model):
    id =models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    year = models.DateField(auto_now=False, auto_now_add=False)
    price = models.FloatField()
    type = models.CharField(max_length=10)