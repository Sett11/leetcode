class Solution:
    def maxProfit(self,a):
        if len(a)==1:
            return 0
        return max(a)
    
s=Solution()

print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([2,4,1]))