from django.apps import AppConfig


class SummarizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'summarizer'

    def ready(self):
        import summarizer.signals 
