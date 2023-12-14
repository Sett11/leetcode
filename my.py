class Solution:
    def superPow(self,a,b):
        return pow(a,int(''.join(map(str,b))),1337)
    
S=Solution()

print(S.superPow(2,[1,0]))