
#import just for show
import pprint
my_printer = pprint.PrettyPrinter(width=10)
class Meta(type):
    def __new__(cls, name, bases, dct):
            x = super().__new__(cls, name, bases, dct)
            x.attr = 100
            return x

class Foo (metaclass=Meta):
    pass


x=Foo()

#this is i the new level not the init level but we can do the same
print (f"Foo = {pprint.pformat(dir(Foo))}")

#this supports intalisense as well!
print (f"x.attr = {x.attr}")



#decorator the more elegent way
def meta_decorator(cls):
    class NewClass(cls):
        attr = 100
    return NewClass

class No_attr_class():
    pass

print (f"No_attr_class = {pprint.pformat(dir(No_attr_class))}")

@meta_decorator
class With_attr_class(No_attr_class):
    pass

new_decorated_class=With_attr_class()
print (f'new_decorated_class attr {new_decorated_class.attr}')
