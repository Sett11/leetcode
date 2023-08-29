class Solution:
    def findKthLargest(self,a,n):
        return sorted([i for i in a],reverse=True)[n-1]
    
s=Solution()

print(s.findKthLargest([3,2,1,5,6,4],2))