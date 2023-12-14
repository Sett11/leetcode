from itertools import product

class Solution:
    def kthSmallestPrimeFraction(self,a,n):
        return sorted([[i[0]/i[1],i] for i in product(a,a) if i[0]!=i[1]])[n-1][1]
    
S=Solution()

print(S.kthSmallestPrimeFraction([1,2,3,5],3))