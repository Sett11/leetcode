class Solution:
    def vowelStrings(self,a,n,m):
        s='aioue'
        return len([i for i in a[n:m+1] if i[0].lower() in s and i[-1].lower() in s])
    
s=Solution()

print(s.vowelStrings(["are","Amy","u"],0,2))