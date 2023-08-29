class Solution:
    def longestCommonPrefix(self,s):
        s=[''.join(set(i)) for i in zip(*s)]
        for i in range(len(s)):
            if len(s[i])>1:
                return ''.join(s[:i])
        return ''.join(s)
    
s=Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix([""]))
print(s.longestCommonPrefix(["a"]))