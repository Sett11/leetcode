from random import shuffle

class Solution:
    def __init__(self,a):
        self.a=a

    def reset(self):
        return self.a

    def shuffle(self):
        t=self.a.copy()
        shuffle(t)
        return t
    
s=Solution([1,2,3])

print(s.shuffle())