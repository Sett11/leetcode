class Solution:
    def findMaxK(self,a):
        try:
            return next(i for i in sorted(a,reverse=True) if -i in a)
        except:
            return -1

s=Solution()

print(s.findMaxK([-1,10,6,7,-7,1]))