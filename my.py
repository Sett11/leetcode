from re import split

class Solution:
    def numDifferentIntegers(self,s):
        return len({int(i) for i in split(r'\D',s) if i})
    
s=Solution()

print(s.numDifferentIntegers('a123bc34d8ef34'))
print(s.numDifferentIntegers('a1b01c001'))