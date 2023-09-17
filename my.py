class Solution:
    def binaryGap(self,n):
        a=[i for i,j in enumerate(bin(n)[2:]) if j=='1']
        m=0
        for i in range(1,len(a)):
            m=max(m,a[i]-a[i-1])
        return m
    
s=Solution()

print(s.binaryGap(22))