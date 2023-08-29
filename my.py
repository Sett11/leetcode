class Solution:
    def longestPalindrome(self,s):
        if len(set(s))==1:
            return s
        o,m={},0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                t=s[i:j]
                if t==t[::-1]:
                    o[len(t)]=t
                    m=max(m,len(t))
        return o[m]
    
s=Solution()

print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome('abb'))