class Solution:
    def kthSmallest(self,a,k):
        return sorted(sum(a,[]))[k-1]

s=Solution()

print(s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))