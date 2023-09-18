class Solution:
    def validPalindrome(self,s):
        if s==s[::-1]:
            return True
        c=s[::-1]
        for i in range(len(s)):
            t=s[:i]+s[i+1:]
            p=c[:-(i+1)]+(c[-i:] if i else '')
            if t==p:
                return True
        return False
    
s=Solution()

print(s.validPalindrome('abca'))
print(s.validPalindrome('deeee'))