class Solution:
    def rangeBitwiseAnd(self,l,r):
        n=0
        while l<r:
            l>>=1
            r>>=1
            n+=1
        return l<<n
    
s=Solution()

print(s.rangeBitwiseAnd(0,0))
print(s.rangeBitwiseAnd(5,7))
print(s.rangeBitwiseAnd(1,2147483647))