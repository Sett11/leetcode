class Solution:
    def uniquePaths(self,m,n):
        if m==1 or n==1:
            return 1
        a=[[0]*n for _ in range(m)]
        for i in range(1,n):
            a[1][i]=1
        for i in range(1,m):
            a[i][1]=1
        for i in range(2,m):
            for j in range(2,n):
                a[i][j]=a[i][j-1]+a[i-1][j]
        return sum(sum(a,[]))+1
        
s=Solution()

print(s.uniquePaths(28,34))