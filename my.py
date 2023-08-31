class Solution:
    def transpose(self,m):
        return [list(i) for i in zip(*m)]
    
s=Solution()

print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))