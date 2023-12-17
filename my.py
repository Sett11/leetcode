def f(n):
    c=0
    while n>1:
        n=3*n+1 if n&1 else n//2
        c+=1
    return c

class Solution:
    def getKth(self,l,r,n):
        return sorted([[f(i),i] for i in range(l,r+1)],key=lambda x:(x[0],x[1]))[n-1][1]

S=Solution()

print(S.getKth(12,15,2))