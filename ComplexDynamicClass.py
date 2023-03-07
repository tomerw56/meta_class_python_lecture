def f(obj):
    print('attr =', obj.attr)

Foo = type('Foo',(),
{
'attr': 100,
'attr_val': f
})

x=Foo()
x.attr=100
x.attr_val()