class Solution:
    def checkString(self,s):
        return 'b' not in s or 'a' not in s[s.index('b'):]
    
s=Solution()

print(s.checkString('aaabbb'))
print(s.checkString('abab'))
print(s.checkString('aaa'))
print(s.checkString('bbb'))
print(s.checkString(''))