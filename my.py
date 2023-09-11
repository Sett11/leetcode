def check(n):
    return [i for i in str(n) if not n%int(i)]

class Solution:
    def countDigits(self,n):
        return len(check(n))
    
s=Solution()

print(s.countDigits(121))