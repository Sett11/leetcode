class Solution:
    def smallestEvenMultiple(self,n):
        return next(i for i in range(n,10000000) if not i%2 and not i%n)

s=Solution()

print(s.smallestEvenMultiple(5))