from functools import reduce as r

class ProductOfNumbers:

    def __init__(self):
        self.a=[]
        self.o={}

    def add(self,n):
        self.a.append(n)
    
    def getProduct(self,k):
        if k in self.o and self.o[k][0]==len(self.a):
            return self.o[k][1]
        v=r(lambda a,c:a*c,self.a[-k:])
        self.o[k]=[len(self.a),v]
        return v
    
p=ProductOfNumbers()

p.add(7)
print(p.getProduct(1))
p.add(5)
p.add(0)
p.add(4)

print(p.getProduct(2))

print(p.getProduct(4))
print(p.getProduct(1))