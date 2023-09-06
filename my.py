from random import choice

class Solution:
    def __init__(self,a):
        self.a=a

    def pick(self,t):
        return choice([i for i,j in enumerate(self.a) if j==t])
    
s=Solution([1, 2, 3, 3, 3])

print(s.pick(3))
print(s.pick(1))
print(s.pick(3))