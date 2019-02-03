from __future__ import absolute_import

from okGoogle.intents import intent
from okGoogle.responseBuilder import ResponseTools, ResponseBuilder
from okGoogle.requestParser import RequestParser


@intent(projectId='djangook-e6a5a')
def Hello_World(request):
    output = {
        'fulfillmentText': '<speak>Hello world!</speak>',
    }
    return output


@intent(projectId='djangook-e6a5a')
def Cookies(request):
    reqInfo = RequestParser.getParam(request)
    parms = reqInfo['parms']
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
        if reqInfo['source']=='google':
            message = '<speak>{}</speak>'.format(text)

        output = ResponseBuilder.textResponse(
            message      = message,
            source       = reqInfo['source'],
            userResponse = userResponse,
        )
        return output


@intent(projectId='djangook-e6a5a')
def GameCard(request):
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
