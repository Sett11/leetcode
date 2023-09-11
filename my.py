class Solution:
    def countKDifference(self,a,k):
        l=len(a)
        c=0
        for i in range(l):
            for j in range(i+1,len(a)):
                if abs(a[i]-a[j])==k:
                    c+=1
        return c
    
s=Solution()

print(s.countKDifference([1,2,2,1],1))