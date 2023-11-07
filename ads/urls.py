from django.urls import path, include
from django.urls import path
from .views import LocationViewSet, AdViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('locations', LocationViewSet)
router.register('ads', AdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]
