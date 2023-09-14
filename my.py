class MyHashSet:
    def __init__(self):
        self.hash=set()

    def add(self,k):
        self.hash.add(k)

    def remove(self,k):
        if k in self.hash:
            self.hash.remove(k)

    def contains(self,k):
        return k in self.hash