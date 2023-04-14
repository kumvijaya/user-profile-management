"""Admin module registration with profile.
"""
from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import Profile

class Admin(ModelAdmin):
    """Admin model extended with geo fields to show the single page view all user locations

    Args:
        ModelAdmin (obj): Base model admin object
    """
    geomap_autozoom = "10"
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"

admin.site.register(Profile, Admin)
