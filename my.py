def f(x):
    r=[]
    for i in x:
        r.append(x.index(i))
    return r
class Solution:
    def isIsomorphic(self,s,t):
        return f(s)==f(t)
        
    
s=Solution()

print(s.isIsomorphic("bbbaaaba","aaabbbba"))
print(s.isIsomorphic("papap","titii"))
print(s.isIsomorphic("ab","ca"))