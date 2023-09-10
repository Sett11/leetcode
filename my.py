class Solution:
    def floodFill(self,a,k,t,c):
        m,n,w=len(a),len(a[0]),a[k][t]
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and a[i][j]==w and a[i][j]!=c:
                a[i][j]=c
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        dfs(k,t)
        return a
    
s=Solution()

print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))