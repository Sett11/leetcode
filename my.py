from re import sub

def f(s):
    return [i for i in sub(r'(.)\1*',lambda e:' '+e.group()+' ',s).split(' ') if i]

class Solution:
    def isLongPressedName(self,s,t):
        a,b=f(s),f(t)
        if len(b)!=len(a):
            return False
        for i in range(len(a)):
            if a[i][0]!=b[i][0] or len(a[i])>len(b[i]):
                return False
        return True
    
s=Solution()

print(s.isLongPressedName("alex","aaleex"))
print(s.isLongPressedName("saeed","ssaaedd"))