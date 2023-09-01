class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        a=[i+k for i,j in enumerate(nums) if j==1]
        return all(abs(a[i]-a[i+1])>k for i in range(len(a)-1))
    
s=Solution()

print(s.kLengthApart([1,0,0,0,1,0,0,1],2))
print(s.kLengthApart([1,0,0,1,0,1],2))