class MagicDictionary:
    def __init__(self):
        self.d=[]

    def buildDict(self,d):
        self.d=d

    def search(self,s):
        for i in self.d:
            if len(i)==len(s):
                c=0
                for j in range(len(s)):
                    if i[j]!=s[j]:
                        c+=1
                if c==1:
                    return True
        return False
    
m=MagicDictionary()

m.buildDict(["hello", "leetcode"])

print(m.search("hello"))
print(m.search('hhllo'))
print(m.search('leetcodd'))