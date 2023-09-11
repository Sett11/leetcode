class Solution:
    def findRelativeRanks(self,a):
        check=sorted(a,reverse=True)
        scores={0:'Gold Medal',1:'Silver Medal',2:'Bronze Medal'}
        for i in range(len(a)):
            g=check.index(a[i])
            if scores.get(g,None)!=None:
                a[i]=scores[g]
            else:
                a[i]=str(g+1)
        return a

s=Solution()

print(s.findRelativeRanks([10,3,8,9,4]))