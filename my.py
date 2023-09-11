class Solution:
    def checkPerfectNumber(self,n):
        a=[]
        i=1
        while i<n**.5:
            if not n%i:
                a.extend([i,n/i])
            i+=1
        return sum(a)-n==n
    
s=Solution()

print(s.checkPerfectNumber(28))