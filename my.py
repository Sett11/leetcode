shift=lambda e,c:chr(ord(e)+c)

class Solution:
    def replaceDigits(self,s):
        l=len(s)
        return ''.join([s[i-1]+shift(s[i-1],int(s[i])) for i in range(1,l,2)])+(s[-1] if l&1 else '')
    
s=Solution()

print(s.replaceDigits('a1c1e1'))
print(s.replaceDigits('a1b2c3d4e'))