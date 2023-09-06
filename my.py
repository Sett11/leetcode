class Solution:
    def canConstruct(self,s,t):
        s,t=list(s),list(t)
        for i in s:
            if i in t:
                t.remove(i)
            else:
                return False
        return True
    
s=Solution()

print(s.canConstruct('aa','aab'))