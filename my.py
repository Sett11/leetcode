from re import sub

def check(s):
    if any(i.isdigit() or i.isupper() for i in s):
        return False
    if any(i in s for i in '.,!') and (s[-1].isalpha() or len(sub(r'[^.,!]','',s))>1):
        return False
    if '-' in s:
        if s.count('-')>1:
            return False
        if len(s)<3:
            return False
        i=s.index('-')
        if not i or i==len(s)-1:
            return False
        if not (s[i-1].isalpha() and s[i+1].isalpha()):
            return False
    return True

class Solution:
    def countValidWords(self,a):
        return len([i for i in a.split(' ') if i and check(i)])
    
s=Solution()

print(s.countValidWords("alice and  bob are playing stone-game10"))