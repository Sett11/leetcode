class Solution:
    def thousandSeparator(self,n):
        n=str(n)[::-1]
        return '.'.join([n[i:i+3] for i in range(0,len(n),3)])[::-1]
    

s=Solution()

print(s.thousandSeparator(2**31-1))
print(s.thousandSeparator(1000))
print(s.thousandSeparator(10000))
print(s.thousandSeparator(100000))
print(s.thousandSeparator(1000000))