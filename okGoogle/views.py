from __future__ import absolute_import

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from . import settings
from .intents import IntentsSchema

import json
import re


class ASKView(APIView):
    def handleRequest(self, data, is_auth):
        if not is_auth:
            output = {'fulfillmentText': '<speak>Fulfillment authenticate fail.</speak>',}
            return Response(data=output, status=HTTP_200_OK)
        body          = json.loads(data)
        projectId     = body['session'].split('/')[1]
        intent        = body['queryResult']['intent']['displayName']
        kwargs = {
            'lang'     : body['queryResult']['languageCode'],
            'parms'    : body['queryResult']['parameters'],
        }
        output = IntentsSchema.route(projectId, intent, **kwargs)
        return Response(data=output, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        is_auth = self._validateHeader(request)
        return self.handleRequest(request.body.decode("utf-8"), is_auth)

    def _validateHeader(self, request):
        HEADERS = settings.ACTIONS_ON_GOOGLE['HEADERS']
        for k, v in HEADERS.items():
            reqHeader = 'HTTP_{}'.format(k).upper()
            if reqHeader not in request.META:
                return False
            elif request.META[reqHeader]!=v:
                return False
        return True
