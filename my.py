from re import sub

class Solution:
    def findTheLongestBalancedSubstring(self,s):
        s=[i for i in sub(r'(.)\1*',lambda e:' '+e.group()+' ',s).split(' ') if i]
        m=0
        for i in range(len(s)-1):
            if s[i][0]=='0' and s[i+1][0]=='1':
                m=max(m,min(len(s[i]),len(s[i+1]))*2)
        return m

s = Solution()

print(s.findTheLongestBalancedSubstring('01000111'))