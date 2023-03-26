import collections
from abc import ABCMeta,abstractmethod
from dataclasses import  dataclass

class Base(object, metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
#will not work
#c=Concrete()


'''
What is a container
class Container(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def __contains__(self, x):
        return False

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Container:
            if any("__contains__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
'''

class ContainAllTheThings(object):
    def __contains__(self, item):
        return True

print(issubclass(ContainAllTheThings, collections.Container))
print(isinstance(ContainAllTheThings(), collections.Container))
