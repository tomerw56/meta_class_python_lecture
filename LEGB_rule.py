x = 'global'
def f():
    x = 'enclosing'

    def g():
        x = 'local'
        print(x)
    g()

print("calling f()")
f()


y=20
def change_global_y():
    global y
    y=10

print(y)
change_global_y()
print(y)



