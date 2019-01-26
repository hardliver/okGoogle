from __future__ import absolute_import

from okGoogle.intents import intent


@intent(projectId='djangook-e6a5a')
def HelloWorld(**kwargs):
    output = {
        'fulfillmentText': '<speak>Hello world!</speak>',
    }
    return output


@intent(projectId='djangook-e6a5a')
def Cookies(**kwargs):
    output = {}
    if 'number' in kwargs['parms']:
        numCookie = int(kwargs['parms']['number'])
        text = "{} cookies!".format(numCookie)
        if numCookie==1:
            text = "{} cookie!".format(numCookie)
    else:
        text = "How many cookies?"
    output['fulfillmentText'] = '<speak>{}</speak>'.format(text)
    return output
