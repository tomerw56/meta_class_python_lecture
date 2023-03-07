class foo_1:
    def __init__(self,base:int):
        self.base=base
    def __eq__(self, other):
        return other==self.base

f=foo_1(base=12)
print (12==f)