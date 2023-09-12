from functools import reduce as r

def d(n):
    i=2
    s=set()
    while i<n*n:
        while n%i==0:
            n//=i
            s.add(i)
        i+=1
    return list(s)

class Solution:
    def distinctPrimeFactors(self,a):
        return len(d(r(lambda e,c:e*c,a)))
    
s=Solution()

print(s.distinctPrimeFactors([i for i in range(1,10000)]))