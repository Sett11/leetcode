class Solution:
    def sortTheStudents(self,m,k):
        return sorted(m,key=lambda e:-e[k])
    
s=Solution()

print(s.sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]],2))