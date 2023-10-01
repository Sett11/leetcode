class Solution:
    def countGoodTriplets(self,a,b,c,d):
        q=0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                for k in range(j+1,len(a)):
                    if abs(a[i]-a[j])<=b and abs(a[j]-a[k])<=c and abs(a[i]-a[k])<=d:
                        q+=1
        return q
    
s=Solution()

print(s.countGoodTriplets([3,0,1,1,9,7],7,2,3))