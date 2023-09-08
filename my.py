class Solution:
    def detectCapitalUse(self,s):
        return s.islower() or s.isupper() or (s[0].isupper() and s[1:].islower())
    
s=Solution()

print(s.detectCapitalUse('Google'))