class Trie:
    def __init__(self):
        self.t=[]

    def insert(self,s):
        self.t.append(s)

    def search(self,w):
        return w in self.t

    def startsWith(self,p):
        return bool([i for i in self.t if i.startswith(p)])
    
t=Trie()

t.insert('apple')

print(t.search('apple'))

print(t.startsWith('app'))