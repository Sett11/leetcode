from re import sub

def f(x,c):
    return x if not c else f(''.join([str(len(i))+i[0] for i in sub(r'(.)\1*',lambda e:' '+e.group()+' ',x).split(' ') if i]),c-1)

class Solution:
    def countAndSay(self,n):
        return f('1',n-1)
    
s=Solution()

print(s.countAndSay(10))