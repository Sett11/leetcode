from random import choice

class RandomizedSet:
    def __init__(self):
        self.a=[]

    def insert(self,v):
        q=v in self.a
        if not q:
            self.a.append(v)
        return not q

    def remove(self,v):
        q=v in self.a
        if q:
            self.a.remove(v)
        return q

    def getRandom(self):
        return choice(self.a)
    
r=RandomizedSet()

print(r.insert(7))
print(r.insert(7))
print(r.insert(1))
print(r.insert(2))
print(r.insert(5))

print(r.remove(5))

print(r.getRandom())
print(r.getRandom())