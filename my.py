from random import randint

class Solution:
    def __init__(self,m,n):
        self.m=m
        self.n=n
        self.s=set()

    def flip(self):
        t=[randint(0,self.m-1),randint(0,self.n-1)]
        c='&'.join([str(i) for i in t])
        while c in self.s:
            t=[randint(0,self.m-1),randint(0,self.n-1)]
            c='&'.join([str(i) for i in t])
        self.s.add(c)
        return t

    def reset(self):
        self.s=set()
    
s=Solution(3,1)

print(s.flip())
print(s.flip())
s.reset()

print(s.flip())
print(s.flip())
print(s.flip())