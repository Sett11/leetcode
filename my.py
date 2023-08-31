from itertools import permutations as p

class Solution:
    def getPermutation(self,n,k):
        return ''.join([j for j in p([str(i) for i in range(1,n+1)])][k-1])
    
s=Solution()

print(s.getPermutation(3,3))
print(s.getPermutation(4,9))