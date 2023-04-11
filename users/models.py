from django.db import models
from django.contrib.auth.models import User
from auditlog.registry import auditlog
from location_field.models.plain import PlainLocationField
from django_admin_geomap import GeoItem

class Location(models.Model, GeoItem):
    name = models.CharField(max_length=100)
    lon = models.FloatField()  # longitude
    lat = models.FloatField()  # latitude
    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lon is None else str(self.lat)

# Extending User Model Using a One-To-One Link
class Profile(models.Model, GeoItem):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=6, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    phone_number = models.CharField(max_length=15, blank=True)

    @property
    def geomap_latitude(self):
        if not self.location:
            return ''
        latitude, _ = self.location.split(',')
        return latitude
    
    @property
    def geomap_longitude(self):
        if not self.location:
            return ''
        _, longitude = self.location.split(',')
        return longitude

    @property
    def name(self):
        return self.user.username

    def __str__(self):
        return self.user.username

auditlog.register(Profile)