class Solution:
    def sumOfSquares(self,a):
        l=len(a)
        return sum((j**2 for i,j in enumerate(a) if l%(i+1)==0))


s = Solution()

print(s.sumOfSquares([1,2,3,4]))
