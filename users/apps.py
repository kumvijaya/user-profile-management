"""User app config registration.
"""
from django.apps import AppConfig

class UsersConfig(AppConfig):
    """App config set with users and signals

    Args:
        AppConfig (obj): Base app config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
