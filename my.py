class Solution:
    def threeSum(self,a):
        a.sort()
        s=set()
        for i in range(len(a)-2):
            f=a[i]
            j=i+1
            k=len(a)-1
            while j<k:
                x=a[j]
                y=a[k]
                p=f+x+y
                if p>0:
                    k-=1
                elif p<0:
                    j+=1
                else:
                    s.add((f,x,y))
                    j+=1
                    k-=1
        return s
    
s=Solution()

print(s.threeSum([-1,0,1,2,-1,-4]))