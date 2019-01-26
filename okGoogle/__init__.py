from django.utils.module_loading import autodiscover_modules


default_app_config = 'okGoogle.apps.OkGoogleConfig'


def autodiscover():
    autodiscover_modules('okGoogle')
