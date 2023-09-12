def d(n):
    a=[]
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            a.extend([i,n//i])
    return sorted(a)

def f(a,k):
    m=int(1e9)
    o={}
    o[m]=m
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]*a[j]==k:
                m=min(abs(a[i]-a[j]),m)
                o[m]=[a[i],a[j],[m]]
    return o[m] if m!=1e9 else [0,0,[int(1e9)]]

class Solution:
    def closestDivisors(self,n):
        o={1:[1,2],2:[1,3],3:[2,2],4:[2,3],5:[2,3],6:[2,4]}
        if o.get(n):
            return o[n]
        c,q=f(d(n+1),n+1),f(d(n+2),n+2)
        return c[:2] if c[2][0]<q[2][0] else q[:2]
    
s=Solution()

print(s.closestDivisors(9))