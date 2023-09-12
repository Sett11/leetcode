class Solution:
    def construct2DArray(self,a,m,n):
        r=[]
        if len(a)!=m*n:
            return r
        while a:
            t=[]
            while len(t)<n:
                t.append(a.pop(0))
            r.append(t)
        return r
    
s=Solution()

print(s.construct2DArray([1,2,3,4,5,6,7,8],2,4))
print(s.construct2DArray([1,2,3,4],2,2))