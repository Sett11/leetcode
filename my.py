class Solution:
    def isThree(self,n):
        return len({i for i in range(1,n+1) if not n%i})==3

s=Solution()

print(s.isThree(4))