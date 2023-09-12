class Solution:
    def checkRecord(self,s):
        return s.find('LLL')==-1 and s.count('A')<2
    
s=Solution()

print(s.checkRecord('PPALLL'))
print(s.checkRecord('PPALLP'))