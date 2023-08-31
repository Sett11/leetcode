from math import sqrt,floor
class Solution:
    def isPerfectSquare(self,n):
        return floor(sqrt(n))==sqrt(n)
    
s=Solution()

print(s.isPerfectSquare(8))
print(s.isPerfectSquare(4))