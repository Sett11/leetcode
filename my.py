class Solution:
    def pivotInteger(self,n):
        c=n-1
        if n==1:
            return 1
        while True:
            if c*(c+1)/2==sum([i for i in range(c,n+1)]) or c==-1:
                return c
            c-=1
    
s=Solution()

print(s.pivotInteger(1))