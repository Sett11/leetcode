from itertools import product
from re import sub,I
class Solution:
    def letterCasePermutation(self,s):
        ns=sub(r'[a-z]','&',s,flags=I)
        a=[list(j) for j in product(*[[i.lower(),i.upper()] for i in s if i.isalpha()])]
        r=[]
        for i in a:
            t=ns
            while i:
                t=t.replace('&',i.pop(0),1)
            r.append(t)
        return r
    
s=Solution()

print(s.letterCasePermutation('RmR'))
print(s.letterCasePermutation('1a2b'))