from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from django.conf import settings

from .intents import IntentsSchema

import json
import re


class ASKView(APIView):
    def handle_request(self, data, is_auth):
        if not is_auth:
            output = {'fulfillmentText': '<speak>Fulfillment authenticate fail.</speak>',}
            return Response(data=output, status=HTTP_200_OK)
        body          = json.loads(data)
        projectId     = body['session'].split('/')[1]
        intent        = body['queryResult']['intent']['displayName']
        lang          = body['queryResult']['languageCode']
        parms         = body['queryResult']['parameters']
        output = IntentsSchema.route(projectId, intent, lang, parms)
        return Response(data=output, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            STATIC_TOKEN = settings.STATIC_TOKEN
            is_auth = True if request.META['HTTP_AUTHORIZATION']==STATIC_TOKEN else False
        except:
            is_auth = True
        return self.handle_request(request.body.decode("utf-8"), is_auth)
