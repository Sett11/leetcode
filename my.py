def f(x):
    l=[int(i) for i in list(str(x))]
    s=sum(l)
    return s if len(l)==1 else f(s)

class Solution:
    def addDigits(self,n):
        return f(n)
    
s=Solution()

print(s.addDigits(3849097))