class Solution:
    def climbStairs(self,n):
        a,b=0,1
        c=0
        while c<=n:
            a,b=b,a+b
            c+=1
        return a
    
s=Solution()

print(s.climbStairs(45))