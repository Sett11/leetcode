class Solution:
    def minimizedStringLength(self,s):
        return len(set(s))
    
s=Solution()

print(s.minimizedStringLength("aaabcd"))