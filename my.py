class Solution:
    def addBinary(self,a,b):
        return bin(int(a,2)+int(b,2))[2:]

s=Solution()

print(s.addBinary('1010','1011'))