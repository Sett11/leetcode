from math import ceil

def e(n):
    n+=1
    r=[True]*n
    r[0]=r[1]=False
    for i in range(2,int(n**.5+1)):
        if r[i]:
            r[2*i:n:i]=[False]*ceil((n/i)-2)
    return [i for i,j in enumerate(r) if j]

p=e(10**6+100)


def left(n):
    l,r=0,len(p)
    while r-l>1:
        m=(r+l)//2
        if p[m]<n:
            l=m
        else:
            r=m
    return l

class Solution:
    def closestPrimes(self,l,r):
        a=p[left(l):]
        if a[0]<l:
            a=a[1:]
        m=10**6
        i=0
        o={}
        while a[i+1]<=r:
            s=a[i+1]-a[i]
            if s in [1,2]:
                return [a[i],a[i+1]]
            m=min(s,m)
            if s not in o:
                o[s]=[a[i],a[i+1]]
            i+=1
        return o[m] if o else [-1,-1]

S=Solution()

print(S.closestPrimes(1,10))
print(S.closestPrimes(19,31))