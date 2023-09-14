class MyHashMap:
    def __init__(self):
        self.map={}

    def put(self,k,v):
        self.map[k]=v

    def get(self,k):
        return self.map.get(k,-1)

    def remove(self,k):
        if k in self.map:
            del self.map[k]

M=MyHashMap()

M.put(1,1)
M.put(2,2)

print(M.get(1))
print(M.get(3))

M.put(2,1)

print(M.get(2))

M.remove(2)

print(M.get(2))