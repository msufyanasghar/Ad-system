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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        locations = serializer.validated_data.get('locations', [])
        for location in locations:
            max_daily_visitors = location.max_daily_visitors
            if max_daily_visitors and self._get_total_daily_visitors(location) > max_daily_visitors:
                return Response(
                    {"error": f"Exceeds maximum daily visitors limit for {location.name}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Custom logic to handle location constraints on update
        locations = serializer.validated_data.get('locations', instance.locations.all())
        for location in locations:
            max_daily_visitors = location.max_daily_visitors
            # Check if the total daily visitors exceed the maximum allowed
            if max_daily_visitors and self._get_total_daily_visitors(location) > max_daily_visitors:
                return Response(
                    {"error": f"Exceeds maximum daily visitors limit for {location.name}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        self.perform_update(serializer)
        return Response(serializer.data)

    def _get_total_daily_visitors(self, location):
        return 0