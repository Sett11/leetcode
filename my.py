class Solution:
    def removeElement(self,l,n):
        i=c=0
        while i<len(l):
            if l[i]==n:
                l.pop(i)
            else:
                c+=1
                i+=1
        return c


s=Solution()

print(s.removeElement([3,2,3,2],3))