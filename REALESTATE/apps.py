from django.apps import AppConfig


class RealestateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'REALESTATE'


    def ready(self):
        import REALESTATE.signals