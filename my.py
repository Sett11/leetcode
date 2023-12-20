class Solution:
    def oddCells(self,n,m,a):
        r=[[0]*m for _ in range(n)]
        def row(a,k):
            for i in range(len(a[k])):
                a[k][i]+=1
        def column(a,k):
            for i in range(len(a)):
                a[i][k]+=1
        for i,j in a:
            row(r,i)
            column(r,j)
        return len([i for i in sum(r,[]) if i&1])
    

S=Solution()

print(S.oddCells(2,3,[[0,1],[1,1]]))