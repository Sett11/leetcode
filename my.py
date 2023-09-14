class Skiplist:
    def __init__(self):
        self.a=[]

    def search(self,t):
        return t in self.a

    def add(self,n):
        self.a.append(n)

    def erase(self,n):
        if n in self.a:
            self.a.remove(n)
            return True
        return False
    
s=Skiplist()