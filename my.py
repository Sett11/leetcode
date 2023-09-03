class Solution:
    def solve(self,a):
        if not a:
            return
        m,n=len(a),len(a[0])
        def dfs(i,j):
            if i<0 or i>=m or j>=n or a[i][j]!='O':
                return
            a[i][j]='&'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if a[i][j]=='O':
                    a[i][j]='X'
                if a[i][j]=='&':
                    a[i][j]='O'
        return a

s=Solution()

print(s.solve([["X","X","X","X"],["X","O","O","X"],["X","X", "O","X"],["X","O","X","X"]]))
print(s.solve([["O","X","O","O","O","X"],
               ["O","O","X","X","X","O"],
               ["X","X","X","X","X","O"],
               ["O","O","O","O","X","X"],
               ["X","X","O","O","X","O"],
               ["O","O","X","X","X","X"]]))
# print(s.solve([["O","X","O","O","O","O","O","O","O"],
#                ["O","O","O","X","O","O","O","O","X"],
#                ["O","X","O","X","O","O","O","O","X"],
#                ["O","O","O","O","X","O","O","O","O"],
#                ["X","O","O","O","O","O","O","O","X"],
#                ["X","X","O","O","X","O","X","O","X"],
#                ["O","O","O","X","O","O","O","O","O"],
#                ["O","O","O","X","O","O","O","O","O"],
#                ["O","O","O","O","O","X","X","O","O"]]))