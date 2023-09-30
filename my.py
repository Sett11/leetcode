class Solution:
    def findLucky(self,a):
        return max([i for i in a if i==a.count(i)],default=-1)

s=Solution()

print(s.findLucky([1,2,2,3,3,3]))