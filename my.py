from re import sub
class Solution:
    def hammingWeight(self,n):
        return len(sub(r'[^1]','',bin(n)))
    
s=Solution()

print(s.hammingWeight(0b00000000000000000000000000001011))