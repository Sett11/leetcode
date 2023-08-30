class Solution:
    def repeatedSubstringPattern(self,s):
        l=len(s)//2
        while l:
            t=s[:l]
            if ''.join([t]*(len(s)//len(s[:l])))==s:
                return True
            l-=1
        return False
    
s=Solution()

print(s.repeatedSubstringPattern('abcabc'))
print(s.repeatedSubstringPattern('abc'))
print(s.repeatedSubstringPattern('a'))