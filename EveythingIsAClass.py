class Foo:
    pass


obj = Foo()
print(f"obj.__class__ {obj.__class__}")
print(f"type(obj) {type(obj)}")
print(f"obj.__class__ is type(obj) {obj.__class__ is type(obj)}")
print(f"isinstance(obj, Foo) {isinstance(obj, Foo)}")
print(f"isinstance(Foo,type) {isinstance(Foo,type)}")

n = 5
d = {'x': 12, 'y': 33}
for item in (n, d, obj):
    print(f"{type(item)} -- is class {type(item) is item.__class__}")

# what will happen if I ask this question?
print(f"type of obj is {type(obj)} but type of Foo is {type(Foo)}")
for item in int, float, dict, list, tuple:
    print(f"{item.__name__} {type(item)}")

#but this bages the question
print(f"{type.__name__} {type(type)}")



