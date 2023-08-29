class Solution:
    def applyOperations(self,a):
        i,r=0,[]
        while i<len(a)-1:
            if a[i]==a[i+1] and a[i]:
                a[i]*=2
                a.pop(i+1)
                r.append(0)
            if not a[i]:
                r.append(0)
                a.pop(i)
                i-=1
            i+=1
        return a+r
    
s=Solution()

print(s.applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]))