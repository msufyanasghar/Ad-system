from rest_framework import serializers
from .models import Location, Ad

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'daily_visitors')


class AdSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)
    class Meta:
        model = Ad
        fields = ['id', 'name', 'start_date', 'end_date', 'locations']