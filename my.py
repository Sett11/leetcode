class Solution:
    def strStr(self,s,t):
        return s.find(t)
    
s=Solution()

print(s.strStr('sadbutsad','sad'))
print(s.strStr('leetcode','leeto'))
print(s.strStr('hello','ll'))