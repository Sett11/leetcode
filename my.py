class Solution:
    def commonFactors(self,a,b):
        return len([i for i in range(1,min(a,b)+1) if not a%i and not b%i])
    
s=Solution()

print(s.commonFactors(12,6))