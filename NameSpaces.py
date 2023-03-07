#import just for show
import pprint

#get all builtin types
#The dir() function returns all properties and methods of the specified object, without the values.
# This function will return all the properties and methods,
# even built-in properties which are default for all object
my_printer = pprint.PrettyPrinter(width=10)
my_printer.pprint(f"{dir(__builtins__)}")

#just for show - the built in help
print(dir.__doc__)


#print number of globals before import
print(f"number of globals pre import {len(globals())}")
import numpy as np
print(f"number of globals after import {len(globals())}")
print(f"{globals()['np']}")
#why would this works
print(f" this is strange right? {globals()['np'].abs(-42)}")

#my_printer.pprint(f"np builtins {np.__builtins__}")


#local example


def encrypt(lst):
    secret = []
    for word in lst:
        secret.append(word[::-1])
    ## LOCAL NAMESPACE
    print(f"local namespace {dir()}")
    print(f"locals {locals()}")

    return secret
encrypt(['hello','world'])


#the diffrence between locals and globals

g=globals()

print(f"is global_x in globals {'global_x' in g}")
global_x='hi'
print(f"is global_x in globals {'global_x' in g}")

def locals_are_fixed():
    x=20
    local_dict=locals()
    print('simple local_dict')
    print(local_dict)
    y=30
    print('added local y not seen')
    print(local_dict)
    x=10
    print('set x to 10')
    print(local_dict)
    print("changed on dict itself")
    local_dict['x']=10
    print(local_dict)
    print(f"real new dict {locals()}")


locals_are_fixed()


