import bisect

class KthLargest:
    def __init__(self,k,a):
        self.k=k
        self.a=sorted(a)

    def add(self,v):
        bisect.insort(self.a,v)
        return self.a[-self.k]
    
K=KthLargest(3,[4, 5, 8, 2])

print(K.add(3))
print(K.add(5))
print(K.add(10))
print(K.add(9))
print(K.add(4))