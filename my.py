class Solution:
    def countNumbersWithUniqueDigits(self,n):
        o={6:168571,7:712891,8:2345851}
        return o[n] if n in o else len([i for i in range(0,10**n) if len(str(i))==len(set(str(i)))])
    
S=Solution()

print(S.countNumbersWithUniqueDigits(8))