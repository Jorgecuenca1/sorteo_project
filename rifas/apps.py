from django.apps import AppConfig
import importlib

class RifasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rifas'

    def ready(self):
        importlib.import_module('rifas.signals')

