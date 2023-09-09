from re import sub

class Solution:
    def strongPasswordCheckerII(self,s):
        r=[False]*4+[len(s)>7]
        for i in range(len(s)):
            if s[i].islower():
                r[0]=True
            if s[i].isupper():
                r[1]=True
            if s[i].isdigit():
                r[2]=True
            if s[i] in '!@#$%^&*()-+':
                r[3]=True
        return all(r) and not bool([i for i in sub(r'(.)\1*',lambda e:' '+e.group()+' ',s).split(' ') if len(i)>1])
        
    
s=Solution()

print(s.strongPasswordCheckerII('IloveLe3tcode!'))