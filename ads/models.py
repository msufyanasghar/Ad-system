from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    max_daily_visitors = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    locations = models.ManyToManyField(Location, related_name='ads')

    def __str__(self):
        return self.name