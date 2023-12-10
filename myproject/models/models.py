from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)


class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null = True)


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    

class ClimateData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    year = models.IntegerField()
    temperature = models.FloatField()
    pollution_level = models.FloatField(null=True)
    
    
    