from math import ceil

def er():
    n=10**6
    r=[True]*n
    r[0]=r[1]=False
    for i in range(n):
        if r[i]:
            r[2*i:n:i]=[False]*ceil((n/i)-2)
    return [i for i,j in enumerate(r) if j]

def right(a,n):
    l,r=0,len(a)
    while r-l>1:
        m=(r+l)//2
        if a[m]<=n:
            l=m
        else:
            r=m
    return r


primes=er()
hash=set(primes)


class Solution:
    def findPrimePairs(self,n):
        a=primes[:right(primes,n)]
        r=[]
        for i in a:
            t=n-i
            if i>t:
                break
            if t in hash:
                r.append([i,t])
        return r


    

S=Solution()

print(S.findPrimePairs(10000))