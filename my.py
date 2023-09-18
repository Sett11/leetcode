class Solution:
    def findNumbers(self,a):
        return len(list((i for i in a if not len(str(i))&1)))
    
s=Solution()

print(s.findNumbers([12,345,2,6,7896]))