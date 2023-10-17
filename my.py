from re import sub

class Solution:
    def removeTrailingZeros(self,s):
        return sub(r'0+$','',s)
    
s=Solution()

print(s.removeTrailingZeros('51230100'))