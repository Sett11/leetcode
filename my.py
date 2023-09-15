class Solution:
    def hasAlternatingBits(self,n):
        s=bin(n)[2:]
        for i in range(len(s)):
            t=s[i:i+2]
            if len(t)>1 and len(set(t))==1:
                return False
        return True
    
s=Solution()

print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(4))
print(s.hasAlternatingBits(11))