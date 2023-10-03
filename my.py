from functools import reduce as r

class Solution:
    def arraySign(self,a):
        s=r(lambda e,u:e*u,a)
        return 1 if s>0 else 0 if not s else -1

s=Solution()

print(s.arraySign([-1,-2,-3,-4,3,2,1]))