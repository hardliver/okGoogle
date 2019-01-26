from __future__ import absolute_import


class IntentsSchema():
    apps = {}
    intents = {}

    @classmethod
    def get_intent(cls, projectId, intent):
        key_name = projectId + "." + intent
        return cls.intents[key_name]

    @classmethod
    def route(cls, projectId, intent, **kwargs):
        """Routes an intent to the proper method"""
        func = cls.get_intent(projectId, intent)
        return func(**kwargs)

    @classmethod
    def register(cls, func, intent, projectId="base"):
        cls.intents[projectId + '.' + intent] = func
        if projectId not in cls.apps:
            cls.apps[projectId] = []
        cls.apps[projectId] += [intent]


def intent(*args, **kwargs):
    """
    Decorator that registers a function to the IntentsSchema
    app - The specific app grouping you'd like to register this intent to - Default: base
    intent - The intent you'd like to give this intent - Default: <The function name>
    """
    invoked = bool(not args or kwargs)
    if not invoked:
        func, args = args[0], ()

    def register(func):
        projectId = kwargs.get('projectId', "base").lower()
        intent = kwargs.get('intent', func.__name__)
        IntentsSchema.register(func, intent, projectId)
        return func
    return register if invoked else register(func)
