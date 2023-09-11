def check(n):
    return all(not n%int(i) for i in str(n))

class Solution:
    def selfDividingNumbers(self,l,r):
        return [i for i in range(l,r+1) if '0' not in str(i) and check(i)]
    
s=Solution()

print(s.selfDividingNumbers(1,10000))