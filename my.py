class Solution:
    def sumOfMultiples(self,n):
        return sum([i for i in range(1,n+1) if any(i%j==0 for j in [3,5,7])])

s = Solution()

print(s.sumOfMultiples(10))
