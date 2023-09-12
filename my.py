from itertools import permutations as p

class Solution:
    def reorderedPowerOf2(self,n):
        for i in p(str(n)):
            t=''.join(i)
            q=int(t)
            if t[0]!='0' and q&(q-1)==0:
                return True
        return False
    
s=Solution()

print(s.reorderedPowerOf2(1024))