class Solution:
    def canPlaceFlowers(self,a,n):
        c,l=0,len(a)
        if l==1 and not a[0]:
            return l>=n
        if l>1 and not a[0] and not a[1]:
            c=1
            a[0]=1
        if l>1 and not a[-1] and not a[-2]:
            c+=1
            a[-1]=1
        for i in range(1,l-1):
            if all([not i for i in [a[i-1],a[i],a[i+1]]]):
                a[i]=1
                c+=1
        return c>=n
    
s=Solution()

print(s.canPlaceFlowers([0,0,1,0,1],1))
print(s.canPlaceFlowers([1,0,0,0,1],2))