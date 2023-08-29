class Solution:
    def wordPattern(self,p,s):
        return [p.index(i) for i in p]==[s.split(' ').index(i) for i in s.split(' ')]
    
s=Solution()

print(s.wordPattern('abba','dog cat cat dog'))