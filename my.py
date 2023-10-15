class Solution:
    def kItemsWithMaximumSum(self,a,b,c,k):
        return sum(([1]*a+[0]*b+[-1]*c)[:k])
    
s=Solution()

print(s.kItemsWithMaximumSum(3,2,0,4))