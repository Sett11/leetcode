class Solution:
    def isPowerOfFour(self,n):
        while n>=4:
            if n%4:
                break
            n/=4
        return n==1
    
s=Solution()

print(s.isPowerOfFour(64))