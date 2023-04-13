from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import Profile, Location

""" Admin model extended with geo fields to show the single page view all user locations
"""
class Admin(ModelAdmin):
    geomap_autozoom = "10"
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"

"""Register the profile and with extended admin model
"""
admin.site.register(Profile, Admin)


