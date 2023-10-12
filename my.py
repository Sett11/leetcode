class Solution:
    def leftRightDifference(self,a):
        return [abs(sum(a[:i])-sum(a[i+1:])) for i in range(len(a))]
    
s=Solution()

print(s.leftRightDifference([10,4,8,3]))