class Solution:
    def minDeletionSize(self,a):
        return len([i for i in zip(*a) if sorted(i)!=list(i)])
    
s=Solution()

print(s.minDeletionSize(["cba","daf","ghi"]))