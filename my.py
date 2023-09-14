class Solution:
    def numSpecial(self,a):
        c=0
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j]==1:
                    a[i][j]=0
                    if 1 not in a[i]+[list(k) for k in zip(*a)][j]:
                        c+=1
                    a[i][j]=1
        return c
    
s=Solution()

print(s.numSpecial([[1,0,0]
                    ,[0,0,1]
                    ,[1,0,0]]))
print(s.numSpecial([[1,0,0],[0,1,0],[0,0,1]]))