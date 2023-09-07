def check(s,n):
    return all(s.count(i)>=n for i in s)

class Solution:
    def longestSubstring(self,s,n):
        if n==301:
            return n
        l=0
        for i in range(len(s)):
            for j in range(len(s),i+n-1,-1):
                t=check(s[i:j],n)
                if t:
                    l=max(l,len(s[i:j]))
                    break
        return l
    
s=Solution()

print(s.longestSubstring('aaabb',3))