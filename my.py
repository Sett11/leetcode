from random import choice

class Solution:
    def sortColors(self,a):
        def hs(a):
            if len(a)<2:
                return a
            l,m,r,n=[],[],[],choice(a)
            {l.append(i) if i<n else r.append(i) if i>n else m.append(i) for i in a}
            return hs(l)+m+hs(r)
        b=hs(a)
        for i in range(len(b)):
            a[i]=b[i]
    
S=Solution()

print(S.sortColors([2,0,2,1,1,0]))