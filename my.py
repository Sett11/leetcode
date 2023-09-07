class Solution:
    def tribonacci(self,n):
        k,a,b,c=0,0,1,1
        while k<n:
            a,b,c=b,c,a+b+c
            k+=1
        return a
    
s=Solution()

print(s.tribonacci(78))