class Solution:
    def numberOfSteps(self,n):
        c=0
        while n:
            if n&1:
                n-=1
            else:
                n//=2
            c+=1
        return c

S=Solution()

print(S.numberOfSteps(14))