class Solution:
    def largestOddNumber(self,s):
        for i in range(len(s)-1,-1,-1):
          if s[i] in '13579':
            return s[:i+1]
        return ''