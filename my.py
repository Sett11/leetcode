class Solution:
    def checkValid(self,a):
        return all(sorted(i)==[x for x in range(1,len(a)+1)] for i in a+[list(j) for j in zip(*a)])
    
s=Solution()

print(s.checkValid([[1,2,3],[3,1,2],[2,3,1]]))