class transaction():
    def __init__(self,name:str,amount:int):
        self.name=name
        self.amount=amount

class balance():

    def __init__(self):
        self._transactions={}

    def add_transaction(self,t:transaction):
        self._transactions[t.name]=t.amount
    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]


b=balance()
b.add_transaction(transaction("111",1))
b.add_transaction(transaction("112",2))
b.add_transaction(transaction("113",1))
b.add_transaction(transaction("114",17))

print(b["111"])
print(len(b))

