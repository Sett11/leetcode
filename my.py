from functools import reduce
from operator import mul

class Solution:
    def subtractProductAndSum(self,n):
        a=list(map(int,str(n)))
        return reduce(mul,a)-sum(a)
    

S=Solution()

print(S.subtractProductAndSum(4421))