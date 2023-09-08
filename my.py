class Solution:
    def isSameAfterReversals(self,n):
        return int(str(int(str(n)[::-1]))[::-1])==n
    
s=Solution()

print(s.isSameAfterReversals(526))
print(s.isSameAfterReversals(1800))