class Solution:
    def shortestPalindrome(self,s):
        l,t=len(s)-1,''
        while t+s!=(t+s)[::-1]:
            t=s[l:][::-1]
            l-=1
        return t+s
    
s=Solution()

print(s.shortestPalindrome('aacecaaa'))
print(s.shortestPalindrome('abcd'))