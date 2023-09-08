class LRUCache:
    def __init__(self,size):
        self.size=size
        self.cache={}
        self.sorted_cache=[]

    def get(self,k):
        if self.cache.get(k,None)!=None:
            i=self.sorted_cache.index(k)
            self.sorted_cache.append(self.sorted_cache.pop(i))
            return self.cache[k]
        return -1

    def put(self,k,v):
        if len(self.cache)==self.size and k not in self.cache:
            e=self.sorted_cache.pop(0)
            del self.cache[e]
        if k in self.sorted_cache:
            self.sorted_cache.append(self.sorted_cache.pop(self.sorted_cache.index(k)))
        else:
            self.sorted_cache.append(k)    
        self.cache[k]=v
    
l=LRUCache(2)

print(l.put(2,1))
print(l.put(1,1))
print(l.put(2,3))
print(l.put(4,1))
print(l.get(2))