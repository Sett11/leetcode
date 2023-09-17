class Solution:
    def shortestToChar(self,s,t):
        g=[i for i,j in enumerate(s) if j==t]
        r=[]
        for i,j in enumerate(s):
            m=1e9
            for j in g:
                m=min(m,abs(i-j))
            r.append(m)
        return r
    
s=Solution()

print(s.shortestToChar('loveleetcode','e'))