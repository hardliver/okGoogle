from __future__ import absolute_import


class ResponseBuilder:
    @classmethod
    def createResponse(
            self,
            message='',
            source=None,
            userResponse=False,
            **kwargs
        ):
        '''
        Shortcut to create response for Actions on Google V2 API

        Parameters:
        message: Text message to be spoken out by the Google home
                 Please checkout Actions on Google SSML.
                 https://developers.google.com/actions/reference/ssml
        source: Build response depend which source.
        userResponse: Should end this session or wait user response.
                 Default False
        '''
        # Webhook response
        # https://dialogflow.com/docs/fulfillment/how-it-works#webhook_response
        if source=='google':
            output = {
                'payload': {
                    'google': {
                        'expectUserResponse': userResponse,
                        'richResponse': {
                            'items': [
                                {
                                    'simpleResponse': {
                                        'textToSpeech': message,
                                    },
                                },
                            ]
                        },
                    },
                },
            }
        else:
            output = {'fulfillmentText': message}
        return output
