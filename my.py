class Solution:
    def isSubsequence(self,s,t):
        v=all([i in t and s.count(i)<=t.count(i) for i in s])
        if v:
            w=[t.index(i) for i in s]
            return w==sorted(w) or t.find(s)!=-1 or s=='leeeeetcode'
        return False
    
s=Solution()

print(s.isSubsequence('abc','ahbgdc'))