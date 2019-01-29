from __future__ import absolute_import


class RequestParser:
    @classmethod
    def getInfo(self, body):
        params = {
            'lang'     : body['queryResult']['languageCode'],
            'parms'    : body['queryResult']['parameters'],
        }
        return params

    @classmethod
    def googleInfoParser(self, body):
        params = {
            'userId': body['originalDetectIntentRequest']['payload']['user']['userId']
        }
        return params

    @classmethod
    def lineInfoParser(self, body):
        params = {
            'userId': body['originalDetectIntentRequest']['payload']['data']['source']['userId']
        }
        return params

    @classmethod
    def getParam(self, body, *args, **kwargs):
        # Webhook request
        # https://dialogflow.com/docs/fulfillment/how-it-works#webhook_request
        source = body['originalDetectIntentRequest']['source']

        params = {'source': source}
        params.update(self.getInfo(body))
        if source=='google':
            params.update(self.googleInfoParser(body))
        elif source=='line':
            params.update(self.lineInfoParser(body))
        return params
