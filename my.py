class Solution:
    def countPairs(self,a,k):
        l=len(a)
        c=0
        for i in range(l):
            for j in range(i+1,l):
                if a[i]==a[j] and not i*j%k:
                    c+=1
        return c
    
s=Solution()

print(s.countPairs([3,1,2,2,2,1,3],2))