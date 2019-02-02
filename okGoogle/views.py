from __future__ import absolute_import

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from . import settings
from .intents import IntentsSchema
from .requestParser import RequestParser

import json
import re


class ASKView(APIView):
    def handleRequest(self, request):
        # Webhook request
        # https://dialogflow.com/docs/fulfillment/how-it-works#webhook_request
        if not self._validateHeader(request):
            output = {'fulfillmentText': '<speak>Fulfillment authenticate fail.</speak>',}
            return Response(data=output, status=HTTP_200_OK)
        body          = json.loads(request.body.decode("utf-8"))
        projectId     = body['session'].split('/')[1]
        intent        = body['queryResult']['intent']['displayName'].replace(' ', '_')
        params = RequestParser.getParam(body)
        output = IntentsSchema.route(projectId, intent, request, **params)
        return Response(data=output, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.handleRequest(request)

    def _validateHeader(self, request):
        HEADERS = settings.ACTIONS_ON_GOOGLE['HEADERS']
        for k, v in HEADERS.items():
            reqHeader = 'HTTP_{}'.format(k).upper()
            if reqHeader not in request.META:
                return False
            elif request.META[reqHeader]!=v:
                return False
        return True
