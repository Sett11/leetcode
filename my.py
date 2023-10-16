class Solution:
    def findColumnWidth(self,a):
        return [max([len(str(j)) for j in i]) for i in zip(*a)]


s = Solution()

print(s.findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]]))
