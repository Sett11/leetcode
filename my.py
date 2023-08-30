class Solution:
    def flipAndInvertImage(self,m):
        return [[0 if j==1 else 1 for j in i[::-1]] for i in m]
    
s=Solution()

print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))