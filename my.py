from re import sub

def rep(a,s):
    r=sorted([i for i in a if s.startswith(i)],key=len)
    return s if not r else r[0]

class Solution:
    def replaceWords(self,a,s):
        return sub(r'\b([A-z])+\b',lambda e:rep(a,e.group()),s)
    
s=Solution()

print(s.replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery"))
print(s.replaceWords(["a","b","c"],"aadsfasf absbs bbab cadsfafs"))