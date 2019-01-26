from django.apps import AppConfig


class OkGoogleConfig(AppConfig):
    name = 'okGoogle'

    def ready(self):
        super(OkGoogleConfig, self).ready()
        self.module.autodiscover()
