class Solution:
    def isPowerOfThree(self,n):
        while n>=3:
            if n%3:
                break
            n/=3
        return n==1
    
s=Solution()

print(s.isPowerOfThree(33))