def f(n,k,j,s):
    c=0
    for i in range(len(s)):
        if k<0 or k>=n or j<0 or j>=n:
            return c-1
        elif s[i]=='U':
            k-=1
            if k<0 or k>=n:
                return c
        elif s[i]=='D':
            k+=1
            if k<0 or k>=n:
                return c
        elif s[i]=='R':
            j+=1
            if j<0 or j>=n:
                return c
        elif s[i]=='L':
            j-=1
            if j<0 or j>=n:
                return c
        c+=1
    return c
class Solution:
    def executeInstructions(self,n,p,s):
        r=[]
        for i in range(len(s)):
            r.append(f(n,p[0],p[1],s[i:]))
        return r
    
s=Solution()

print(s.executeInstructions(3,[0,1],'RRDDLU'))