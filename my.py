class Solution:
    def sumOfThree(self,n):
        m=n//3
        s=m-1+m+m+1
        return [m-1,m,m+1] if s==n else []
    
S=Solution()

print(S.sumOfThree(33))
print(S.sumOfThree(43))