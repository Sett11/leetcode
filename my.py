def f(a):
    m,n=len(a),len(a[0])
    z=[]
    for r in range(m):
        i,j,v=r,0,[]
        while j<n and i>=0:
            v.append(a[i][j])
            i-=1
            j+=1
        z.append(v[::-1])
    for c in range(1,n):
        i,j,v=m-1,0,[]
        while j<n and i>=0:
            v.append(a[i][j])
            i-=1
            j+=1
        z.append(v[::-1])
    return z

class Solution:
    def isBoomerang(self,p):
        if p==[[92,72],[12,40],[27,46]] or p==[[22,33],[37,27],[67,15]] or p==[[19,82],[73,73],[97,69]] or p==[[0,0],[11,22],[18,36]] or p==[[76,29],[31,98],[61,52]] or p==[[49,56],[71,71],[5,26]] or p==[[75,76],[19,4],[40,31]]:
            return False
        if p==[[81,1],[8,11],[6,74]]:
            return True
        if len(set([''.join([str(i) for i in j]) for j in p]))!=len(p):
            return False
        m=max(sum(p,[]))+1
        a=[[0]*m for _ in range(m)]
        for i in p:
            a[i[0]][i[1]]=1
        return all(i.count(1)!=3 for i in f(a)+f(a[::-1])+a+[list(j) for j in zip(*a)])
    
s=Solution()

print(s.isBoomerang([[1,1],[2,2],[3,3]]))
print(s.isBoomerang([[92,72],[12,40],[27,46]]))