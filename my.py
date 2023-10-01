class Solution:
    def unequalTriplets(self,a):
        q=0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                for k in range(j+1,len(a)):
                    if a[i]!=a[j] and a[j]!=a[k] and a[i]!=a[k]:
                        q+=1
        return q
    
s=Solution()

print(s.unequalTriplets([4,4,2,4,3]))