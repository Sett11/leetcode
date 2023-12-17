from functools import cache

@cache
def f(n):
    r=[1,n]
    for i in range(2,int(n**.5+1)):
        if n%i==0:
            if i not in r and n//i not in r:
                r.extend([i,n//i])
    return sum(r) if len(set(r))==4 else 0

class Solution:
    def sumFourDivisors(self,a):
        return sum(list(map(f,a)))

S=Solution()

print(S.sumFourDivisors([21,21]))