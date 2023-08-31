from itertools import permutations as p
class Solution:
    def permute(self,a):
        return [list(i) for i in p(a)]
    
s=Solution()

print(s.permute([1,15,6,3]))