class Solution:
    def kthLargestNumber(self,a,n):
        return str(sorted([int(i) for i in a],reverse=True)[n-1])
    
s=Solution()

print(s.kthLargestNumber(["2","21","12","1"],3))