from collections import Counter as c

class Solution:
    def isFascinating(self,n):
        s=str(n)+str(n*2)+str(n*3)
        r=set(c(s).values())
        return all(i in s for i in '123456789') and len(r)==1 and 1 in r and '0' not in s
    
s=Solution()

print(s.isFascinating(192))