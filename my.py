from itertools import permutations
from bisect import insort

class Solution:
    def findEvenNumbers(self,a):
        s=set((permutations(a,3)))
        r=[]
        for i in s:
            n=int(''.join([str(j) for j in i]))
            if not n&1 and n>=100:
                insort(r,n)
        return r
    
s=Solution()

print(s.findEvenNumbers([2,1,3,0]))
print(s.findEvenNumbers([2,2,8,8,2]))