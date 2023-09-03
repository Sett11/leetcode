import re

class Solution:
    def reverseVowels(self,s):
        a=[i for i in s if i.lower() in 'aeoiu'][::-1]
        s=re.sub(r'[aioue]','&6&',s,flags=re.I)
        for i in a:
            s=s.replace('&6&',i,1)
        return s
        
s=Solution()

print(s.reverseVowels('leetcode'))