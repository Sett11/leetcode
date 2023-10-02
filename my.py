from re import sub

class Solution:
    def reformat(self,s):
        a,b=sub(r'\d','',s),sub(r'\D','',s)
        if abs(len(a)-len(b))>1 or (not a and len(s)>1) or (not b and len(s)>1):
            return ''
        if len(a)>len(b):
            a,b=b,a
        if len(b)>len(a):
            a,b=b,a
        c=''
        j=0
        for i in a:
            c+=i
            if j<len(b):
                c+=b[j]
            j+=1
        return c
        
    
s=Solution()

print(s.reformat('a'))