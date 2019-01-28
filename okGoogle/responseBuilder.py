from __future__ import absolute_import


class ResponseBuilder:
    @classmethod
    def createResponse(
            self,
            message='',
            userResponse=False,
            **kwargs
        ):
        '''
        Shortcut to create response for Actions on Google V2 API

        Parameters:
        message: Text message to be spoken out by the Google home
                 Please checkout Actions on Google SSML.
                 https://developers.google.com/actions/reference/ssml
        userResponse: Should end this session or wait user response.
                 Default False
        '''
        # Webhook response
        # https://dialogflow.com/docs/fulfillment/how-it-works#webhook_response
        output = {
            'fulfillmentText': message,
            'payload': {
                'google': {
                    'expectUserResponse': userResponse,
                },
            },
        }
        return output
