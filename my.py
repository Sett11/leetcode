class Solution:
    def getHint(self,s,q):
        c=x=i=0
        s,q=list(s),list(q)
        while i<(min(len(s),len(q))):
            if s[i]==q[i]:
                c+=1
                s.pop(i)
                q.pop(i)
                i-=1
            i+=1
        i=0
        while i<len(s):
            if s[i] in q:
                x+=1
                q.pop(q.index(s[i]))
                s.pop(i)
                i-=1
            i+=1
        return f'{c}A{x}B'

s=Solution()

print(s.getHint('1807','7810'))
print(s.getHint('1123','0111'))