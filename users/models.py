from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from auditlog.registry import auditlog
from location_field.models.plain import PlainLocationField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_admin_geomap import GeoItem

"""Location model to store the location info with name.
"""
class Location(models.Model, GeoItem):
    name = models.CharField(max_length=100)
    lon = models.FloatField()
    lat = models.FloatField()

    """Gets longitude.

    Returns:
        str: longitude data
    """
    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    """Gets latitude.
    
    Returns:
        str: latitude data
    """
    @property
    def geomap_latitude(self):
        return '' if self.lon is None else str(self.lat)

"""User profile (extened user info) for adding custom attributes (address, phone, location) to user.
Extended User Model Using a One-To-One Link
"""
class Profile(models.Model, GeoItem):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=6, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    phone_number = models.CharField(max_length=15, blank=True)

    """Gets geo map latitude.

    This parses location to retrive the latitude
    Returns:
        str: latitude data
    """
    @property
    def geomap_latitude(self):
        if not self.location:
            return ''
        latitude, _ = self.location.split(',')
        return latitude
    
    """Gets geo map longitude.

    This parses location to retrive the longitude
    Returns:
        str: longitude data
    """
    @property
    def geomap_longitude(self):
        if not self.location:
            return ''
        _, longitude = self.location.split(',')
        return longitude

    """Gets profile name.

    Returns:
        str: profile name
    """
    @property
    def name(self):
        return self.user.username

    """Gets object's display string.

    Returns:
        str: user name as object display string
    """
    def __str__(self):
        return self.user.username

"""Registering profile with audit log to get the profile field updates log.
"""
auditlog.register(Profile)