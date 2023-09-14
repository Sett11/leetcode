class MapSum:
    def __init__(self):
        self.o={}

    def insert(self,k,v):
        self.o[k]=v

    def sum(self,p):
        c=0
        for i in self.o:
            if i.startswith(p):
                c+=self.o[i]
        return c

M=MapSum()

M.insert('apple',3)

print(M.sum('ap'))

M.insert('app',4)

print(M.sum('ap'))