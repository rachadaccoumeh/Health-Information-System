from django.apps import AppConfig


class HospConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hosp'


class ApiauthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apiauthentication'
