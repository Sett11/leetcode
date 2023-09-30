class Solution:
    def maximum69Number (self,n):
        m=n
        a=list(str(n))
        for i in range(len(a)):
            if a[i]=='6':
                t=a.copy()
                t[i]='9'
                m=max(m,int(''.join(t)))
        return m

s=Solution()

print(s.maximum69Number(9669))