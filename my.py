class Solution:
    def singleNumber(self,a):
        for i in set(a):
            if a.count(i)==1:
                return i
    
s=Solution()

print(s.singleNumber([0,1,0,1,0,1,99]))