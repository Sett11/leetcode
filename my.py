from math import sqrt

class Solution:
    def countTriples(self,n):
        a=[i for i in range(1,n+1)]
        c=0
        for i in range(len(a)):
            for j in range(len(a)):
                q=sqrt(a[i]**2+a[j]**2)
                if q in a:
                    c+=1
        return c
    
s=Solution()

print(s.countTriples(300))