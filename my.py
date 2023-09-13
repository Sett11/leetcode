class Solution:
    def minimumCost(self,a):
        a=sorted(a,reverse=True)
        c=0
        m=-1
        while a:
            t=k=-1
            if a:
                t=a.pop(0)
                c+=t
                m=max(t,m)
            if a:
                k=a.pop(0)
                c+=k
                m=max(k,m)
            if a and a[0]<=m:
                a.pop(0)
            if a and a[0]>m:
                c+=a.pop(0)
        return c
    
s=Solution()

print(s.minimumCost([6,5,7,9,2,2]))
print(s.minimumCost([1,2,3]))