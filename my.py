class Solution:
    def findDuplicate(self,a):
        r=set()
        for i in a:
            if i in r:
                return i
            r.add(i)
    
s=Solution()

print(s.findDuplicate([1,3,4,2,2]))