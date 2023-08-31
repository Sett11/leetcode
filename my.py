from itertools import permutations as p
class Solution:
    def permuteUnique(self,a):
        return [[int(n) for n in k.split('&')] for k in set(['&'.join([str(j) for j in i]) for i in p(a)])]
    
s=Solution()

print(s.permuteUnique([1,1,2]))
print(s.permuteUnique([1,2,3,4,4,5]))