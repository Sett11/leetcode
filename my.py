class Solution:
    def countPairs(self,a,n):
        c=0
        l=len(a)
        for i in range(l):
            for j in range(i+1,l):
                if a[i]+a[j]<n:
                    c+=1
        return c


s = Solution()

print(s.countPairs([-1,1,2,3,1],2))
