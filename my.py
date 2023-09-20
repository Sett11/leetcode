def f(a,v):
    for i in range(len(a)-1):
        if (v and a[i]>=a[i+1]) or (not v and a[i]<=a[i+1]):
            return False
    return True

class Solution:
    def validMountainArray(self,a):
        n=a.index(max(a))
        return bool(a[:n] and a[n+1:] and f(a[:n],True) and f(a[n+1:],False) and a.count(a[n])==1)
    
s=Solution()

print(s.validMountainArray([0,3,2,1]))
print(s.validMountainArray([2,1]))