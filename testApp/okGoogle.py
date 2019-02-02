from __future__ import absolute_import

from okGoogle.intents import intent
from okGoogle.responseBuilder import ResponseTools, ResponseBuilder


@intent(projectId='djangook-e6a5a')
def Hello_World(request, **kwargs):
    output = {
        'fulfillmentText': '<speak>Hello world!</speak>',
    }
    return output


@intent(projectId='djangook-e6a5a')
def Cookies(request, parms, **kwargs):
    if 'number' in parms:
        if parms['number']:
            numCookie = int(parms['number'])
            userResponse = False
            text = "{} cookies!".format(numCookie)
            if numCookie==1:
                text = "{} cookie!".format(numCookie)
        else:
            userResponse = True
            text = "How many cookies?"

        message = text
        if kwargs['source']=='google':
            message = '<speak>{}</speak>'.format(text)

        output = ResponseBuilder.textResponse(
            message      = message,
            source       = kwargs['source'],
            userResponse = userResponse,
        )
        return output

@intent(projectId='djangook-e6a5a')
def GameCard(request, parms, **kwargs):
    image   = ResponseTools.getStaticLink(request, 'DarkMagicianGirl.jpg')
    buttons = [
      {
        'text': 'Django okGoogle',
        'postback': 'https://github.com/hardliver/okGoogle'
      },
    ]
    return ResponseBuilder.cardResponse(
        title        = 'Dark Magician Girl',
        subtitle     = 'Yu-Gi-Oh!',
        text         = 'Sorry, your device not support this infomations',
        imageUrl     = image,
        buttons      = buttons
    )
