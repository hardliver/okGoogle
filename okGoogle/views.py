from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .intents import IntentsSchema

import json
import re


class ASKView(APIView):
    def handle_request(self, data):
        body          = json.loads(data)
        projectId     = body['session'].split('/')[1]
        intent        = body['queryResult']['intent']['displayName']
        lang          = body['queryResult']['languageCode']
        parms         = body['queryResult']['parameters']

        output = IntentsSchema.route(projectId, intent, lang, parms)
        return Response(data=output, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.handle_request(request.body.decode("utf-8"))
