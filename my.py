class Solution:
    def imageSmoother(self,a):
        m,n=len(a),len(a[0])
        r=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                q=[]
                for k in range(i-1,i+2):
                    for h in range(j-1,j+2):
                        if 0<=k<m and 0<=h<n:
                            q.append(a[k][h])
                r[i][j]=sum(q)//len(q)
        return r
    
s=Solution()

print(s.imageSmoother([[100,200,100],
                       [200,50,200],
                       [100,200,100]]))
print(s.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))