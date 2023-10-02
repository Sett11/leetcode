from re import sub

class Solution:
    def reformatNumber(self,s):
        s=sub(r'\D','',s)
        r=[]
        while len(s)>4:
            r.append(s[:3])
            s=s[3:]
        r='-'.join(r)
        if len(s)==4:
            return r+('-' if r else '')+s[0:2]+'-'+s[2:4]
        return r+('-' if r else '')+s
    
s=Solution()

print(s.reformatNumber('123 4-567'))