class Solution:
    def rowAndMaximumOnes(self,a):
        return sorted([[j.count(1),i] for i,j in enumerate(a)],key=lambda e:(e[0],-e[1]),reverse=True)[0][::-1]

s = Solution()

print(s.rowAndMaximumOnes([[0,0],[1,1],[0,0],[1,1]]))