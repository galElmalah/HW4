def make_class(attrs, base=None):
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    def set(name, value):
        attrs[name] = value

    def new(*args):
        attrs = {}
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        def set(name, value):
            attrs[name] = value


        obj = {'get': get, 'set': set}
        init = get('__init__')
        if init: init(*args)
        return obj

    cls = {'get': get, 'set': set, 'new': new}
    return cls
