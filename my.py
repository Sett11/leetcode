class Solution:
    def distinctDifferenceArray(self,a):
        return [len(set(a[:i]))-len(set(a[i:])) for i in range(1,len(a)+1)]
    
s=Solution()

print(s.distinctDifferenceArray([1,2,3,4,5]))