from re import sub

def f(s):
    a=[i for i in sub(r'\#+',lambda e:' '+e.group()+' ',s).split(' ') if i]
    g=[i for i,j in enumerate(a) if j[0]=='#' and i]
    for i in g:
        a[i-1]=a[i-1][:-len(a[i])]
        a[i]=''
        if i<len(a)-1:
            a[i+1]=a[i-1]+a[i+1]
            a[i-1]=''
    return ''.join(a).replace('#','')

class Solution:
    def backspaceCompare(self,s,t):
        return f(s)==f(t)
    
s=Solution()

print(s.backspaceCompare("ab#c","ad#c"))
print(s.backspaceCompare("a##c","#a#c"))