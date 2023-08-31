class Solution:
    def alternateDigitSum(self,n):
        return eval('+'.join(['(+'+i+')' if j%2==0 else '(-'+i+')' for j,i in enumerate(list(str(n)))]))
    
s=Solution()

print(s.alternateDigitSum(886996))