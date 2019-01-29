from __future__ import absolute_import

from okGoogle.intents import intent
from okGoogle.responseBuilder import ResponseBuilder


@intent(projectId='djangook-e6a5a')
def Hello_World(**kwargs):
    print(kwargs)
    output = {
        'fulfillmentText': '<speak>Hello world!</speak>',
    }
    return output


@intent(projectId='djangook-e6a5a')
def Cookies(parms, **kwargs):
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
        return ResponseBuilder.createResponse(
            message      = '<speak>{}</speak>'.format(text),
            userResponse = userResponse,
        )
