def f(a,x,y):
    i,j=x,y
    r=[]
    while j>=0:
        if a[i][j]==1:
            r.append([i,j])
            break
        j-=1
    i,j=x,y
    while j<8:
        if a[i][j]==1:
            r.append([i,j])
            break
        j+=1
    i,j=x,y
    while i>=0:
        if a[i][j]==1:
            r.append([i,j])
            break
        i-=1
    i,j=x,y
    while i<8:
        if a[i][j]==1:
            r.append([i,j])
            break
        i+=1
    i,j=x,y
    while i<8 and j>=0:
        if a[i][j]==1:
            r.append([i,j])
            break
        i+=1
        j-=1
    i,j=x,y
    while i>=0 and j>=0:
        if a[i][j]==1:
            r.append([i,j])
            break
        i-=1
        j-=1
    i,j=x,y
    while i<8 and j<8:
        if a[i][j]==1:
            r.append([i,j])
            break
        i+=1
        j+=1
    i,j=x,y
    while i>=0 and j<8:
        if a[i][j]==1:
            r.append([i,j])
            break
        i-=1
        j+=1
    return r

class Solution:
    def queensAttacktheKing(self,a,b):
        c=[[0]*8 for _ in range(8)]
        c[b[0]][b[1]]=2
        for i in range(8):
            for j in range(8):
                if [i,j] in a:
                    c[i][j]=1
        return f(c,b[0],b[1])
    
S=Solution()

print(S.queensAttacktheKing([[0,0],[1,1],[2,2],[3,4],[3,5],[ 4,4],[4,5]],[3,3]))