from bisect import bisect,bisect_left

class Solution:
    def maximumCount(self,a):
        return max(len(a[:bisect_left(a,0)]),len(a[bisect(a,0):]))
    
s=Solution()

print(s.maximumCount([-2,-1,-1,1,2,3]))
print(s.maximumCount([-3,-2,-1,0,0,1,2]))
print(s.maximumCount([1,2,3,4]))