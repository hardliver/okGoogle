from __future__ import absolute_import

from django.conf.urls import url
from .views import ASKView


urlpatterns = [
    url(r'^ask/', ASKView.as_view(), name='okGoogle'),
]
