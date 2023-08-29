class Solution:
    def firstUniqChar(self,s):
        for i in sorted(set(s),key=s.index):
            if s.count(i)<2:
                return s.index(i)
        return -1
    
s=Solution()

print(s.firstUniqChar('leetcode'))