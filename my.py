class Solution:
    def findDiagonalOrder(self,a):
        if len(a)==1 or (a and len(a[0])==1):
            return sum(a,[])
        m,n,r,r2=len(a),len(a[0]),[],[]
        w,c=[],2
        if m==2 and n>2:
            r.append([a[0][0]])
            for i in range(1,n):
                if i&1:
                    r.append([a[0][i],a[1][i-1]])
                else:
                    r.append([a[1][i-1],a[0][i]])
            r.append([a[1].pop()])
            return sum(r,[])
        while c:
            for i in range(m):
                j,k,z=i,0,[]
                while k<n and j>=0:
                    z.append(a[j][k])
                    j-=1
                    k+=1
                t=sorted(z)
                if t not in w:
                    if c==2:
                        r.append(z)
                    else:
                        r2.append(z[::-1])
                    w.append(t)
            c-=1
            a=[h[::-1] for h in a[::-1]]
        res=r+r2[::-1]
        for i in range(1,len(res),2):
            res[i]=res[i][::-1]
        return sum(res,[])
    
s=Solution()

print(s.findDiagonalOrder([[1,2,3],
                           [4,5,6],
                           [7,8,9]]))

print(s.findDiagonalOrder([[2,5],
                           [8,4],
                           [0,-1]]))

print(s.findDiagonalOrder([[2,5,8],
                           [4,0,-1]]))

print(s.findDiagonalOrder([[1,2,3,4],
                           [5,6,7,8],
                           [9,10,11,12]]))
print(s.findDiagonalOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13]]))

print(s.findDiagonalOrder([[1,2,3,4,5,6,7,8,9,10],
                           [11,12,13,14,15,16,17,18,19,20]]))