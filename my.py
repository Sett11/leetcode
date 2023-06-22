class Solution:
    def countOperationsToEmptyArray(self,l):
        c=0
        while len(l):
            if(min(l)==l[0]):
                l.pop(0)
                c+=1
            else:
                l.append(l.pop(0))
                c+=1
        return c

r=Solution()
print(r.countOperationsToEmptyArray([3,4,-1]))