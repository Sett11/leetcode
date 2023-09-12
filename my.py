from math import ceil

class Solution():
    def countOdds(self,l,r):
        return ceil((r-l)/2)+(1 if r&1 and l&1 else 0)
    
s=Solution()

print(s.countOdds(3,7))
print(s.countOdds(8,10))
print(s.countOdds(5,7))
print(s.countOdds(21,22))