class Solution:
    def numIdenticalPairs(self,a):
        l=len(a)
        c=0
        for i in range(l):
            for j in range(i+1,l):
                if a[i]==a[j]:
                    c+=1
        return c
    
s=Solution()

print(s.numIdenticalPairs([1,2,3,1,1,3]))