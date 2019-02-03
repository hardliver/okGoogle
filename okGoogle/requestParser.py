from __future__ import absolute_import

import json


class RequestParser:
    @classmethod
    def _getInfo(self, body):
        params = {
            'lang'     : body['queryResult']['languageCode'],
            'parms'    : body['queryResult']['parameters'],
        }
        return params

    @classmethod
    def _googleInfoParser(self, body):
        params = {
            'userId': body['originalDetectIntentRequest']['payload']['user']['userId']
        }
        return params

    @classmethod
    def _lineInfoParser(self, body):
        params = {
            'userId': body['originalDetectIntentRequest']['payload']['data']['source']['userId']
        }
        return params

    @classmethod
    def getParam(self, request):
        # Webhook request
        # https://dialogflow.com/docs/fulfillment/how-it-works#webhook_request
        body = self.getRawParam(request)
        try:
            source = body['originalDetectIntentRequest']['source']
        except:
            source = None
        params = {'source': source}
        params.update(self._getInfo(body))
        if source=='google':
            params.update(self._googleInfoParser(body))
        elif source=='line':
            params.update(self._lineInfoParser(body))
        return params

    @classmethod
    def getRawParam(self, request):
        '''
        Get all infomations that google request
        '''
        return json.loads(request.body.decode("utf-8"))
