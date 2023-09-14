from re import sub

class NestedIterator:
    def __init__(self,a):
        self.a=[i for i in sub(r'[^\d -]','',str(a)).split(' ') if i]
    
    def next(self):
        return int(self.a.pop(0))
    
    def hasNext(self):
         return bool(self.a)
    
N=NestedIterator([[1,-1],2,[1,[-1]]])

print(N.next())
print(N.next())
print(N.next())
print(N.hasNext())