from django.db import models
from django.contrib.auth.models import User
# from location_field.models.plain import PlainLocationField


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=100, blank=True)
    address_line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=6, blank=True)
    # location = PlainLocationField(based_fields=['city'], zoom=7)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username
