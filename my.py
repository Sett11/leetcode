from math import sqrt,floor
class Solution:
    def mySqrt(self,n):
        return floor(sqrt(n))
    
s=Solution()

print(s.mySqrt(8))
print(s.mySqrt(4))