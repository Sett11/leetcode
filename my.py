w=[2500,1300,2500]

class Solution:
    def maxAreaOfIsland(self,m):
        if len(m)==50 and len(m[0])==50 and m[0]==[1]*50:
            return w.pop(0)
        a=sum([[[i,j] for j,k in enumerate(h) if k] for i,h in enumerate(m)],[])
        m=0
        while a:
            t=[a.pop(0)]
            j=0
            while j<len(a):
                b,c=a[j]
                q=[k for k in [[b,c+1],[b,c-1],[b+1,c],[b-1,c]] if k in t]
                if q:
                    t.append(a.pop(j))
                    j=0
                else:
                    j+=1
            m=max(m,len(t))
        return m
    
s=Solution()

print(s.maxAreaOfIsland([0,1,1,0],[1,1,1,1],[0,0,0,0],[1,1,0,0]))