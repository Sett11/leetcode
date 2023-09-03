class Solution:
    def numIslands(self,a):
        m,n=len(a),len(a[0])
        q=[[False]*n for _ in range(m)]
        c=0
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or a[i][j]=='0' or q[i][j]:
                return
            q[i][j]=True
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        for i in range(m):
            for j in range(n):
                if a[i][j]=='1' and not q[i][j]:
                    dfs(i,j)
                    c+=1
        return c
        
    
s=Solution()

print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
print(s.numIslands([["1","1","1","1","1","1"],
                    ["1","0","0","0","0","1 "],
                    ["1","0","1","1","0","1"],
                    ["1","0","0","0","0", "1"],
                    ["1","1","1","1","1","1"]]))