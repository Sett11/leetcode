class Solution:
    def arithmeticTriplets(self,a,d):
        l=len(a)
        c=0
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if a[j]-a[i]==d and a[k]-a[j]==d:
                        c+=1
        return c
    
s=Solution()

print(s.arithmeticTriplets([0,1,4,6,7,10],3))