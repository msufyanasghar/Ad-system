# ads/views.py
from rest_framework import generics
from .models import Location, Ad
from .serializers import LocationSerializer, AdSerializer
from datetime import date
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_blocked=False, start_date__lte=date.today(), end_date__gte=date.today())
        location = self.request.query_params.get('location')
        location_object = get_object_or_404(Location, id=location)
        if location:
            queryset = queryset.filter(locations__id=location, location__daily_visitors__lt=location_object.daily_visitor_limit)
            return queryset
        return Response({'message':'Location parameter is required'},status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        instance = super().get_object()
        location = self.request.query_params.get('location')
        location_object = get_object_or_404(Location, id=location)
        instance = get_object_or_404(Ad, id=instance.id, locations=location_object, daily_visitors__lt=location_object.daily_visitor_limit)
        location_object.daily_visitors += 1
        location_object.save()
        return instance