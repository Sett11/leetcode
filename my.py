class Solution:
    def peakIndexInMountainArray(self,a):
        return a.index(max(a))
    
s=Solution()

print(s.peakIndexInMountainArray([1,2,3,1]))