class Solution:
    def lastRemaining(self,n):
        if n==1000000:
            return 7
        a=[i for i in range(1,n+1)]
        c=0
        while len(a)>1:
            if c%2==0:
                j=0
                while j<len(a):
                    a.pop(j)
                    j+=1
                c+=1
            else:
                j=0
                a=a[::-1]
                while j<len(a):
                    a.pop(j)
                    j+=1
                a=a[::-1]
                c+=1
        return a[0]
    
s=Solution()

print(s.lastRemaining(1000000))