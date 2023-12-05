class Solution:
    def orangesRotting(self,a):
        n,m=len(a),len(a[0])
        v,c=n*m,0

        while v:
            r=[]
            w=False
            for i in range(n):
                for j in range(m):
                    if a[i][j]==1:
                        w=True
                    if a[i][j]==2:
                        p=[[k,h] for k,h in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]] if -1<k<n and -1<h<m and a[k][h]==1]
                        r.extend(p)
            
            for x,y in r:
                a[x][y]=2

            if not w:
                return c
            
            c+=1
            v-=1
        
        return -1
    

S=Solution()

print(S.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(S.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))