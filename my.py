class Solution:
    def matrixReshape(self,a,m,n):
        b=sum(a,[])
        if len(b)!=m*n:
            return a
        r=[]
        while b:
            t=[]
            while len(t)<n:
                t.append(b.pop(0))
            r.append(t)
        return r
    
s=Solution()

print(s.matrixReshape([[1,2],[3,4],[5,6],[7,8]],2,4))
print(s.matrixReshape([[1,2],[3,4]],1,4))