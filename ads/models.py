from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    daily_visitors = models.IntegerField(default=0)
    daily_visitor_limit = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    locations = models.ManyToManyField(Location, related_name='ads')
    is_blocked = models.BooleanField(default=False)


    def __str__(self):
        return self.name

