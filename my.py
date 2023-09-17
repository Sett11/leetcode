def f(a,b):
    n=min(a,b)
    while n>1:
        if a%n==0 and b%n==0:
            return False
        n-=1
    return True

class Solution:
    def simplifiedFractions(self,n):
        a=[i for i in range(1,n+1)]
        r=[]
        for i in range(n):
            for j in range(i+1,n):
                if f(a[i],a[j]):
                    r.append(f'{a[i]}/{a[j]}')
        return r
    
s=Solution()

print(s.simplifiedFractions(4))