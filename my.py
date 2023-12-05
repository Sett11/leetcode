from collections import defaultdict

class Solution:
    def longestArithSeqLength(self,a):
        o=defaultdict(dict)
        c=1

        for i in range(len(a)):
            for j in range(i):
                n=a[i]-a[j]
                if n not in o[j]:
                    o[j][n]=1
                if n not in o[i]:
                    o[i][n]=0
                o[i][n]=o[j][n]+1
                c=max(c,o[i][n])

        return c
    
S=Solution()

print(S.longestArithSeqLength([20,1,15,3,10,5,8]))