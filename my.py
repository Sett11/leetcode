class Solution:
    def numSteps(self,s):
        n,c=int(s,2),0
        while n!=1:
            n=n+1 if n&1 else n//2
            c+=1
        return c

    
S=Solution()

print(S.numSteps('1101'))