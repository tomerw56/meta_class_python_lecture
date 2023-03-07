#consider this code - see how dynamic type interpertaion works!!
print(type(3))

print(type(['foo', 'bar', 'baz']))
t = (1, 2, 3, 4, 5)
print(type(t))


#define classes the strange way!!
FooDynamic = type('Foo', (), {})
x_dynamic= FooDynamic()

class FooRegular:
    pass
x_regular=FooRegular

#why would this work
print(f" works, {type(x_dynamic)}")
print(f" works as well {x_regular.__name__}, {type(x_regular)}")

#but not this?
print(f"does not work {x_dynamic.__name__}, {type(x_dynamic)}")







