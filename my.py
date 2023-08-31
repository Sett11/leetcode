from re import sub
class Solution:
    def countBits(self,n):
        return [len(sub(r'[^1]','',bin(i))) for i in range(n+1)]
    
s=Solution()

print(s.countBits(10))