def pascal_triangle(n,r):
    if not n:
        return r
    a=[0]*(len(r[-1])+1)
    a[0]=a[-1]=1
    for i in range(1,len(a)-1):
        a[i]=r[-1][i-1]+r[-1][i]
    r.append(a)
    return pascal_triangle(n-1,r)

class Solution:
    def getRow(self,n):
        p=[[1],[1,1],[1,2,1]]
        if n<len(p):
            return p[n]
        return pascal_triangle(n-2,p)[n]

s=Solution()

print(s.getRow(7))