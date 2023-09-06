def f(x):
    return sum([ord(i) for i in x])

class Solution:
    def findTheDifference(self,s,t):
        return chr(f(t)-f(s))
    
s=Solution()

print(s.findTheDifference('abcd','bcade'))