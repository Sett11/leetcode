def d(n):
    i=2
    a=[]
    while i<n*n:
        while n%i==0:
            n//=i
            a.append(i)
        i+=1
    return a

class Solution:
    def smallestValue(self,n):
        a=[]
        while True:
            n=sum(d(n))
            if n in a:
                return n
            else:
                a.append(n)
        return a
    
s=Solution()

print(s.smallestValue(12588))