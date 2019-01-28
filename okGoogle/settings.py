from __future__ import absolute_import

from django.conf import settings
from .exceptions import ActionOnGoogleSettingError


USER_SETTINGS = getattr(settings, 'ACTIONS_ON_GOOGLE', None)

DEFAULT_SETTINGS = {
    'HEADERS': {}
}

def mergeSetting(USER_SETTINGS, DEFAULT_SETTINGS):
    _settings = DEFAULT_SETTINGS
    if type(USER_SETTINGS) is dict:
        for k,v in USER_SETTINGS.items():
            defaultValue = _settings[k]
            if k in _settings:
                if type(v)==type(defaultValue):
                    _settings[k] = v
                else:
                    raise ActionOnGoogleSettingError('{} value type should be {}'.format(k, type(defaultValue).__name__))
    return _settings

ACTIONS_ON_GOOGLE = mergeSetting(USER_SETTINGS, DEFAULT_SETTINGS)
