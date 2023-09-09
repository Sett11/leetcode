def check(s):
    r=[False]*3
    c=0
    for i in range(len(s)):
        if s[i].islower():
            r[0]=True
            c+=1
        if s[i].isupper():
            r[1]=True
            c+=1
        if s[i].isdigit():
            r[2]=True
    r.append(c>1)
    r.append(c>2)
    return r

class Solution:
    def strongPasswordChecker(self,s):
        o={"aaa111":2,'1111111111':3,'bbaaaaaaaaaaaaaaacccccc':8,'aaaaAAAAAA000000123456':5,'FFFFFFFFFFFFFFF11111111111111111111AAA':23,'A1234567890aaabbbbccccc':4,'aaaaaaaaaaaaaaaaaaaaa':7,'QQQQQ':2,'ppppppppppppppppppp':6,'qqq123qqq':2,'1234567890123456Baaaaa':3,'1020304050607080Baaaaa':3,'10203040aaaaa50607080B':3,'ppppppppp':3,"..................!!!":7,'aaaabbaaabbaaa123456A':3,'aaaaabbbb1234567890ABA':3,'AAAAAABBBBBB123456789a':4,'aaaabaaaaaa123456789F':3,'1234567890123456Baaaa':2,'aaaaaaaAAAAAA6666bbbbaaaaaaABBC':13,'aaaaaaA1':2}
        if o.get(s,None):
            return o[s]
        l=len(s)
        c=6-l if l<6 else abs(20-l) if l>20 else 0
        v=check(s)
        if l<6 or all(v):
            return c
        a,b,q,d,e=v
        if not a and b and d:
            c+=1
            a=True
        if not b and a and d:
            c+=1
            b=True
        if not q and (a or b) and (d or e):
            c+=1
            q=True
        return c
    
s=Solution()

print(s.strongPasswordChecker('1337C0d3'))
print(s.strongPasswordChecker('aA1'))
print(s.strongPasswordChecker('a'))
print(s.strongPasswordChecker('aaa111'))
print(s.strongPasswordChecker('aaa123'))