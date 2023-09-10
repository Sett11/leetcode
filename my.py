class Solution:
    def islandPerimeter(self,m):
        a,b=len(m),len(m[0])
        c=0
        for i in range(a):
            for j in range(b):
                if m[i][j]==1:
                    t=[[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
                    l=[m[k[0]][k[1]] for k in t if k[0]>=0 and k[0]<a and k[1]>=0 and k[1]<b and not m[k[0]][k[1]]]
                    c+=len(l)+(1 if not i else 0)+(1 if not j else 0)+(1 if i==a-1 else 0)+(1 if j==b-1 else 0)
        return c
    
s=Solution()

print(s.islandPerimeter([[1]]))
print(s.islandPerimeter([[0,1,0,0],
                         [1,1,1,0],
                         [0,1,0,0],
                         [1,1,0,0]]))