class Solution:
    def findNonMinOrMax(self,a):
        a.remove(min(a))
        if a:
            a.remove(max(a))
        return -1 if not a else a[0]

    
s=Solution()

print(s.findNonMinOrMax([1,2]))
print(s.findNonMinOrMax([1,2,5]))