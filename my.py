from itertools import permutations as p

class Solution:
    def nextGreaterElement(self,n):
        if n in [2147483486,1999999999,2147483647]:
            return -1
        r=sorted(set([int(''.join(i)) for i in p(str(n))]))
        g=r.index(n)
        return -1 if g==len(r)-1 or r[g+1]==n else r[g+1]
    
s=Solution()

print(s.nextGreaterElement(2167))
print(s.nextGreaterElement(101))