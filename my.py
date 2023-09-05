from re import sub

class Solution:
    def removeStars(self,s):
        a=sub(r'\*+',lambda e:' '+e.group()+' ',s).split(' ')
        g=[i for i,j in enumerate(a) if j and j[0]=='*']
        for i in g:
            a[i-1]=a[i-1][:-len(a[i])]
            a[i]=''
            if i<len(a)-1:
                a[i+1]=a[i-1]+a[i+1]
                a[i-1]=''
        return ''.join(a)
    
s=Solution()

print(s.removeStars("leet**cod*e"))
print(s.removeStars("erase*****"))
print(s.removeStars("abb*cdfg*****x*"))