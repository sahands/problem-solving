class my_metaclass(type):
    def __new__(cls, class_name, parents, attributes):
        print "- my_metaclass.__new__ - Creating class instance of type", cls
        return super(my_metaclass, cls).__new__(cls,
                                                class_name,
                                                parents,
                                                attributes)

    def __init__(self, class_name, parents, attributes):
        print "- my_metaclass.__init__ - Initializing the class instance", self
        super(my_metaclass, self).__init__(self)

    def __call__(self, *args, **kwargs):
        print "- my_metaclass.__call__ - Creating object of type ", self
        return super(my_metaclass, self).__call__(*args, **kwargs)


def my_class_decorator(cls):
    print "- my_class_decorator - Chance to modify the class", cls
    return cls


@my_class_decorator
class C(object):
    __metaclass__ = my_metaclass

    def __new__(cls):
        print "- C.__new__ - Creating object."
        return super(C, cls).__new__(cls)

    def __init__(self):
        print "- C.__init__ - Initializing object."


c = C()
print "Object c =", c, type(c)
exit()


frametype_class_dict = {}

class ID3v2FrameClass(object):
    def __init__(self, frame_id):
        self.frame_id = frame_id

    def __call__(self, cls):
        print "Decorating class", cls.__name__
        # Here we could add some helper methods or attributes to c
        if self.frame_id:
            frametype_class_dict[self.frame_id] = cls
        return cls

    @staticmethod
    def get_class_from_frame_identifier(frame_identifier):
        return frametype_class_dict.get(frame_identifier)


@ID3v2FrameClass(None)
class ID3v2Frame(object):
    pass


@ID3v2FrameClass("TIT2")
class ID3v2TitleFrame(ID3v2Frame):
    frame_identifier = "TIT2"


@ID3v2FrameClass("COMM")
class ID3v2CommentFrame(ID3v2Frame):
    frame_identifier = "COMM"


title_class = ID3v2FrameClass.get_class_from_frame_identifier('TIT2')
comment_class = ID3v2FrameClass.get_class_from_frame_identifier('COMM')
print title_class
print comment_class


exit()

frametype_class_dict = {}


class ID3v2FrameClassFactory(object):
    def __new__(cls, class_name, parents, attributes):
        print "Creating class", class_name
        # Here we could add some helper methods or attributes to c
        c = type(class_name, parents, attributes)
        if attributes['frame_identifier']:
            frametype_class_dict[attributes['frame_identifier']] = c
        return c

    @staticmethod
    def get_class_from_frame_identifier(frame_identifier):
        return frametype_class_dict.get(frame_identifier)


class ID3v2Frame(object):
    frame_identifier = None
    __metaclass__ = ID3v2FrameClassFactory
    pass


class ID3v2TitleFrame(ID3v2Frame):
    __metaclass__ = ID3v2FrameClassFactory
    frame_identifier = "TIT2"


class ID3v2CommentFrame(ID3v2Frame):
    __metaclass__ = ID3v2FrameClassFactory
    frame_identifier = "COMM"


title_class = ID3v2FrameClassFactory.get_class_from_frame_identifier('TIT2')
comment_class = ID3v2FrameClassFactory.get_class_from_frame_identifier('COMM')
print title_class
print comment_class


exit()





from decorators_2 import logged


def log_everything_metaclass(class_name, parents, attributes):
    print "Creating class", class_name
    myattributes = {}
    for name, attr in attributes.items():
        myattributes[name] = attr
        if hasattr(attr, '__call__'):
            myattributes[name] = logged("%b %d %Y - %H:%M:%S",
                                        class_name + ".")(attr)
    return type(class_name, parents, myattributes)


class C(object):
    __metaclass__ = log_everything_metaclass

    def __init__(self, x):
        self.x = x

    def print_x(self):
        print self.x


print "Starting object creation!"
c = C("Test!")
c.print_x()
