from __future__ import absolute_import

from django.contrib.staticfiles.templatetags.staticfiles import static


class ResponseTools:
    @classmethod
    def getStaticLink(self, request, path):
        '''
        Get full link of static file

        Parameters:
        path: static file's path
        '''
        ssl  = request.META['HTTP_X_FORWARDED_PROTO']
        host = request.META['HTTP_HOST']
        image = static(path)
        return '{}://{}{}'.format(ssl, host, image)


class ResponseBuilder:
    # Webhook response
    # https://dialogflow.com/docs/fulfillment/how-it-works#webhook_response

    @classmethod
    def textResponse(
            self,
            message='',
            source=None,
            userResponse=False,
            **kwargs
        ):
        '''
        Shortcut to create text response for Actions on Google V2 API

        Parameters:
        message: Text message to be spoken out by the Google home
            Please checkout Actions on Google SSML.
            https://developers.google.com/actions/reference/ssml
        source: Build response depend which source.
        userResponse: Should end this session or wait user response.
            Default False
        '''
        output = {}
        if source=='google':
            output['payload'] = {
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
            }
        else:
            output['fulfillmentText'] = message
        return output

    @classmethod
    def imageResponse(
            self,
            imageUrl,
            text=None,
        ):
        '''
        Shortcut to create image response for Actions on Google V2 API

        Parameters:
        imageUrl: required, image's full link.
            local static file can using ResponseTools.getStaticLink
        text: optional, if user's device not support to show image.
            but check user's device than using textResponse should be better.
        '''
        output = {
          'fulfillmentMessages': [
            {
              'image': {
                'imageUri': imageUrl,
              }
            }
          ],
        }
        if text:
            output['fulfillmentText'] = text
        return output

    @classmethod
    def cardResponse(
            self,
            imageUrl,
            text=None,
            title=None,
            subtitle=None,
            buttons=[],
        ):
        '''
        Shortcut to create card response for Actions on Google V2 API

        Parameters:
        imageUrl: required, image's full link.
            local static file can using ResponseTools.getStaticLink
        text: optional, if user's device not support to show card.
            but check user's device than using textResponse should be better.
        title: optional, if wannna show a full card this param is required.
        subtitle: optional.
        buttons: optional, if wannna show a full card this param is required,
            allow more then two buttons, example:
        [
          {
            'text': 'Django okGoogle',
            'postback': 'https://github.com/hardliver/okGoogle'
          },
        ]
        '''
        output = {
          'fulfillmentMessages': [
            {
              'card': {
                'title'   : title,
                'subtitle': subtitle,
                'imageUri': imageUrl,
                'buttons' : buttons
              }
            }
          ],
        }
        if text:
            output['fulfillmentText'] = text
        return output
