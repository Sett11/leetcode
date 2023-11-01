class Solution:
    def reversePrefix(self,s,c):
        if c not in s:
            return s
        i=s.index(c)
        return s[0:i+1][::-1]+s[i+1:]