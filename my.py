class Solution:
    def checkIfExist(self,a):
        l=len(a)
        for i in range(l):
            t=a[i]*2
            if t in a and a.index(t)!=i:
                return True
        return False
    
s=Solution()

print(s.checkIfExist([10,2,5,3]))
print(s.checkIfExist([3,1,7,11]))
print(s.checkIfExist([-2,0,10,-19,4,6,-8]))