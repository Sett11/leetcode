class Solution:
    def countNegatives(self,a):
        c=0
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j]<0:
                    c+=len(a[i][j:])
                    break
        return c
    
s=Solution()

print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(s.countNegatives([[3,2],[1,0]]))