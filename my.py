class Solution:
    def getCommon(self,a,b):
        return min(set(a).intersection(set(b)),default=-1)
    
s=Solution()

print(s.getCommon([1,2,3],[2,4]))