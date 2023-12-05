from itertools import permutations as p

class Solution:
    def largestTimeFromDigits(self,a):
        a=list(map(lambda x:''.join(map(str,x)),p(a)))
        m=24
        o={}

        for i in a:
            n=float(i[:2]+'.'+i[2:])
            t=24-n
            if t>0 and int(i[2:])<60:
                m=min(m,t)
                o[t]=str(n)
        
        r=(o[m][:2]+':'+o[m][2:]).replace('.','') if m in o else ''
        c=r.split(':')

        if r and len(c[0])<2:
            r='0'+r
        
        if r and len(c[1])<2:
            r+='0'
        
        return r
    
S=Solution()

print(S.largestTimeFromDigits([2,0,6,6]))