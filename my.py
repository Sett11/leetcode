from re import sub

class Solution:
    def sumIndicesWithKSetBits(self,a,k):
        return sum([j for i,j in enumerate(a) if len(sub(r'[^1]','',bin(i)))==k])


s = Solution()

print(s.sumIndicesWithKSetBits([5,10,1,5,2],1))
