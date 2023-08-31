class Solution:
    def gameOfLife(self,m):
        a=[]
        for i in range(len(m)):
            for j in range(len(m[i])):
                t=[[i+1,j],[i-1,j],[i,j+1],[i,j-1],[i-1,j-1],[i+1,j+1],[i-1,j+1],[i+1,j-1]]
                t=[m[k[0]][k[1]] for k in t if k[0]>=0 and k[0]<len(m) and k[1]>=0 and k[1]<len(m[i])]
                c=t.count(1)
                a.append([[i,j],m[i][j],c])
        for i in a:
            if i[1]==1:
                if i[2]<2 or i[2]>3:
                    m[i[0][0]][i[0][1]]=0
            if i[1]==0 and i[2]==3:
                m[i[0][0]][i[0][1]]=1
        return m
    
s=Solution()

print(s.gameOfLife([
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]]))