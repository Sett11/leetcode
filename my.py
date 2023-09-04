from itertools import combinations as c

class Solution:
    def combinationSum3(self,k,n):
        return [list(j) for j in c([i for i in range(1,10) if i<n],k) if sum(j)==n]
    
s=Solution()

print(s.combinationSum3(3,9))