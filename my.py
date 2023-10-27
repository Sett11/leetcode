class Solution:
    def lengthOfLIS(self,a):
        s=0
        n=len(a)
        r=[0]*(n+1)
        for i in range(1,n+1):
            m=0
            for j in range(i):
                if a[i-1]>a[j-1] and r[j]>m:
                    m=r[j]
            r[i]=m+1
            s=max(s,r[i])
        return s

s=Solution()

print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))