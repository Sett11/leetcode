class Solution:
    def getMinDistance(self,a,k,n):
        return min([abs(i-n) for i,j in enumerate(a) if j==k])
    

S=Solution()

print(S.getMinDistance([1,2,3,4,5],5,3))