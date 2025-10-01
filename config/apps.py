from django.apps import AppConfig
import sys

class ConfigConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "config"

    def ready(self):
        # Evita iniciar el scheduler durante migrate/makemigrations
        if "runserver" in sys.argv or "uwsgi" in sys.argv:  
            from employees import scheduler
            scheduler.start()
