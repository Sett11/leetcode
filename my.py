def f(x):
    i=2
    while i<=x:
        if i>6:
            return True
        while x%i==0:
            x//=i
        i+=1
    return False
class Solution:
    def isUgly(self,n):
        return n>0 and not f(n)
    
s=Solution()

print(s.isUgly(6))
print(s.isUgly(14))
print(s.isUgly(905391974))