class Solution:
    def countPrimes(self,n):
        if n<3:
            return 0
        p=[True]*(n+1)
        p[0]=p[1]=False
        for i in range(2,int(n**.5)+1):
            if p[i]:
                for i in range(i*i,n,i):
                    p[i]=False
        r=[i for i in range(2,n) if p[i]]
        return len(r)
        
    
s=Solution()

print(s.countPrimes(1000001))