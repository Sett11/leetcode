from statistics import median as m
class Solution:
    def findMedianSortedArrays(self,a,b):
        return m(sorted(a+b))
    
s=Solution()

print(s.findMedianSortedArrays([1,2],[3,4]))