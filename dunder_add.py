class point():
    def __init__(self,x:int=0,y:int=0):
        self._x=x
        self._y=y


    def add_int(self,const:int):
        self._x+=const
        self._y+=const
    def add_point(self,other_point):
        self._x += other_point._x
        self._y += other_point._y

    def __iadd__(self, other):
        if type(other)==int:
            self.add_int(other)
        else:
            self.add_point(other)
        return point(self._x,self._y)
    def __add__(self, other):
        if isinstance(other,int):
            self.add_int(other)
        else:
            self.add_point(other)

    def __call__(self):
        print(f"Called Point {self._x},{self._y}")

    def __str__(self):
        return f"x ={self._x} y={self._y}"

p1=point(0,0)
print(p1)
p1+=5
print(p1)
p2=point(10,20)
p1+=p2
print(p1)
p1()
p2()

