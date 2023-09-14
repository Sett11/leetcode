from bisect import bisect_left

class Solution:
    def search(self,a,n):
        return bisect_left(a,n) if n in a else -1
    
s=Solution()

print(s.search([-1,0,3,5,9,12],9))
print(s.search([-1,0,3,5,9,12],22))