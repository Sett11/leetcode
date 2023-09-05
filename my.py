class Solution:
    def defangIPaddr(self,s):
        return s.replace('.','[.]')
    
s=Solution()

print(s.defangIPaddr("1.1.1.1"))