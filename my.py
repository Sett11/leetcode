class Solution:
    def findPeakGrid(self,m):
        if len(m)==1:
            return [0,m[0].index(max(m[0]))]
        for i in range(len(m)):
            for j in range(len(m[i])):
                t,r=m[i][j],[i,j]
                if not i:
                    if not j and t>m[i][j+1] and t>m[i+1][j]:
                        return r
                    if j==len(m[i])-1 and t>m[i][j-1] and t>m[i+1][j]:
                        return r
                    if j and j!=len(m[i])-1 and t>m[i][j-1] and t>m[i][j+1] and t>m[i+1][j]:
                        return r
                if i==len(m)-1:
                    if not j and t>m[i-1][j] and t>m[i][j+1]:
                        return r
                    if j==len(m[i])-1 and t>m[i][j-1] and t> m[i-1][j]:
                        return r
                    if t>m[i][j+1] and t>m[i][j-1] and t>m[i-1][j]:
                        return r
                if not j and i and i!=len(m)-1 and t>m[i-1][j] and t>m[i+1][j] and t>m[i][j+1]:
                    return r
                if j==len(m[i])-1 and t>m[i-1][j] and t>m[i+1][j] and t>m[i][j-1]:
                    return r
                if i and j and i!=len(m)-1 and j!=len(m[i])-1 and t>m[i-1][j] and t>m[i+1][j] and t>m[i][j-1] and t>m[i][j+1]:
                    return r
    
s=Solution()

print(s.findPeakGrid([[67]]))
print(s.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))
print(s.findPeakGrid([[10,30,40,50,20],[1,3,2,500,4]]))
print(s.findPeakGrid([[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8, 9,10],[4,5,6,7,8,9,10,11]]))