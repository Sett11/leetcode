class Solution:
    def maxProduct(self,a):
        l=len(a)
        m=0
        for i in range(l):
            for j in range(i+1,l):
                m=max((a[i]-1)*(a[j]-1),m)
        return m
    
s=Solution()

print(s.maxProduct([3,4,5,2]))