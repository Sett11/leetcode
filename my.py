class Solution:
    def checkXMatrix(self,a):
        if not all(sum([[a[i][i],a[i][len(a[0])-1-i]] for i in range(len(a))],[])):
            return False
        for i in range(len(a)):
            a[i][i]=0
            a[i][len(a[0])-1-i]=0
        return all(not i for i in sum(a,[]))
    
s=Solution()

print(s.checkXMatrix([[5,0,0,1],
                      [0,4,1,5],
                      [0,5,2,0],
                      [4,1,0,2]]))