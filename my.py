class Solution:
    def toHex(self,n):
        return hex(n)[2:] if n>=0 else hex(n+2**32)[2:]