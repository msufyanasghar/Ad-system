from django.contrib import admin
from .models import Ad, Location

# Register your models here.
class Ad_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_date', 'end_date',]



class Location_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'daily_visitors']


admin.site.register(Ad, Ad_Admin)
admin.site.register(Location, Location_Admin)
