class Solution:
    def findFinalValue(self,a,n):
        while n in a:
            n*=2
        return n
    
s=Solution()

print(s.findFinalValue([5,3,6,1,12],3))