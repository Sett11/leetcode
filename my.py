class Solution:
    def maxSum(self,a,n,k):
        m=0
        for i in range(len(a)):
            t=a[i:i+k]
            if len(set(t))>=n:
                m=max(m,sum(t))
        return m

s=Solution()

print(s.maxSum([2,6,7,3,1,7],3,4))
print(s.maxSum([5,9,9,2,4,5,4],1,3))