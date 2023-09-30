class Solution:
    def bitwiseComplement(self,n):
        return int(''.join(['1' if i=='0' else '0' for i in bin(n)[2:]]),2)
    
s=Solution()

print(s.bitwiseComplement(5))