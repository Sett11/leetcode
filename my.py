class Solution:
    def onesMinusZeros(self,a):
        m,n=len(a),len(a[0])
        b=[[i.count(0),i.count(1)] for i in zip(*a)]
        a=[[i.count(0),i.count(1)] for i in a]
        r=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r[i][j]=a[i][1]+b[j][1]-a[i][0]-b[j][0]
        return r
    
s=Solution()

print(s.onesMinusZeros([[0,1,1],
                        [1,0,1],
                        [0,0,1]]))