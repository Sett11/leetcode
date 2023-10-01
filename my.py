class Solution:
    def numWaterBottles(self,n,m):
        return int(n+((n-1)/(m-1)))
    
s=Solution()

print(s.numWaterBottles(9,3))
print(s.numWaterBottles(15,4))
print(s.numWaterBottles(15,7))
print(s.numWaterBottles(10,6))