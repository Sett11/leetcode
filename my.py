class Solution:
    def numSquares(self,n):
        d=[float('inf') for _ in range(n+1)]
        d[0]=0
        p=[i**2 for i in range(1,int(n**.5)+1)]
        for i in range(n+1):
            for j in p:
                if i+j<=n:
                    d[i+j]=min(d[i]+1,d[i + j])
                else:
                    break
        return d[n]
    
s=Solution()

print(s.numSquares(22))
print(s.numSquares(2897))