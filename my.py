from math import gcd

def lcm(a,b):
    return a*b/gcd(a,b)

class Solution:
    def nthMagicalNumber(self,n,a,b):
        k,l,r=lcm(a,b),2,10**14

        while l<r:
            m=(l+r)//2
            if m//a+m//b-m//k<n:
                l=m+1
            else:
                r=m
        
        return l%(10**9+7)
    
S=Solution()

print(S.nthMagicalNumber(4,2,3))