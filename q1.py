from make_class import make_class as cls



def make_feets_class():
    def __init__(self, feets):
        if type(feets) is int or type(feets) is float:
            self['set']('value', float(feets))
        elif type(feets) is str:
            tmp = feets.split(" ")
            if(isFloat(tmp[0]) and tmp[1] == "ft"):
                self['set']('value', float(tmp[0]))
            else:
                raise Exception("Format error: {}".format(feets))
        else:
            raise Exception("Type error: {}".format(type(feets)))

    def __str__(self):
        return '{} ft'.format(self['get']('value'))

    def __repr__(self):
        return 'Feets[\'new\']({})'.format(self['get']('value'))

    return cls(locals())


def make_miles_class():
    def __init__(self, miles):
        if type(miles) is int or type(miles) is float:
            self['set']('value', float(miles))
        elif type(miles) is str:
            tmp = miles.split(" ")
            if(isFloat(tmp[0]) and tmp[1] == "mi"):
                self['set']('value', float(tmp[0]))
            else:
                raise Exception("Format error: {}".format(miles))
        else:
            raise Exception("Type error: {}".format(type(miles)))

    def __str__(self):
        return '{} mi'.format(self['get']('value'))

    def __repr__(self):
        return 'miles[\'new\']({})'.format(self['get']('value'))

    return cls(locals())
