class Solution:
    def findIndices(self,a,g,v):
        l=len(a)
        for i in range(l):
            for j in range(i,l):
                if abs(i-j)>=g and abs(a[i]-a[j])>=v:
                    return [i,j]
                    break
        return [-1]*2

s=Solution()

print(s.findIndices([5,1,4,1],2,4))