class Solution:
    def removeElement(self,l,n):
        return  len([i for i in l if i!=n])

r=Solution()
print(r.removeElement([3,2,2,3],3))