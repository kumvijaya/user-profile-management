"""Custom models in users app.
"""
from django.db import models
from django.contrib.auth.models import User
from auditlog.registry import auditlog
from location_field.models.plain import PlainLocationField
from django_admin_geomap import GeoItem

class Location(models.Model, GeoItem):
    """Location model to store the location info with name.

    Args:
        Model (obj): Base model
        GeoItem : Geo model
    """
    name = models.CharField(max_length=100)
    lon = models.FloatField()
    lat = models.FloatField()

    @property
    def geomap_longitude(self):
        """Gets longitude attribute

        Returns:
            str: longitude data
        """
        return '' if self.lon is None else str(self.lon)


    @property
    def geomap_latitude(self):
        """Gets latitude attribute
    
        Returns:
            str: latitude data
        """
        return '' if self.lon is None else str(self.lat)


class Profile(models.Model, GeoItem):
    """User profile (extened user info) for adding custom attributes (address, phone, location).
    Extended User Model Using a One-To-One Link

    Args:
        Model (obj): Base model
        GeoItem : Geo model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=6, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    phone_number = models.CharField(max_length=15, blank=True)

    @property
    def geomap_latitude(self):
        """Gets geo map latitude. This parses location to retrive the latitude

        Returns:
            str: latitude data
        """
        if not self.location:
            return ''
        latitude, _ = self.location.split(',')
        return latitude

    @property
    def geomap_longitude(self):
        """Gets geo map longitude. This parses location to retrive the longitude
        Returns:
            str: longitude data
        """
        if not self.location:
            return ''
        _, longitude = self.location.split(',')
        return longitude

    @property
    def name(self):
        """Gets profile name.

        Returns:
            str: profile name
        """
        return self.user.username

    def __str__(self):
        """Gets object's display string.

        Returns:
            str: user name as object display string
        """
        return self.user.username

# Registering profile with audit log to get the profile field updates log.
auditlog.register(Profile)
