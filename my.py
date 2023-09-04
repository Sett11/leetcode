class Solution:
    def uniquePathsWithObstacles(self,d):
        m,n=len(d),len(d[0])
        a=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if d[0][i]==1:
                break
            else:
                a[0][i]=1
        for i in range(m):
            if d[i][0]==1:
                break
            else:
                a[i][0]=1
        for i in range(1,m):
            for j in range(1,n):
                if d[i][j]==1:
                    continue
                a[i][j]=a[i][j-1]+a[i-1][j]
        return a[-1][-1]
        
s=Solution()

print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
[[0, 0, 0],
 [0, 1, 1],
 [0, 1, 0]]