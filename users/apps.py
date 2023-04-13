from django.apps import AppConfig

""" Added signals to register and listen the events
"""
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self):
        import users.signals  # noqa