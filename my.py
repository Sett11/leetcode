class Solution:
    def makeSmallestPalindrome(self,s):
        i=0
        l=len(s)
        s=list(s)
        while s!=s[::-1]:
            if s[i]!=s[l-i-1]:
                s[i]=s[l-i-1]=min(s[i],s[l-i-1])
            i+=1
        return ''.join(s)


s = Solution()

print(s.makeSmallestPalindrome('abcd'))
