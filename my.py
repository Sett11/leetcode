class Solution:
    def minOperations(self,a,n):
        r=[i for i in range(1,n+1)]
        a=a[::-1]
        for i in range(len(a)+1):
            t=a[:i]
            if all(j in t for j in r):
                return len(t)


s = Solution()

print(s.minOperations([3,1,5,4,2],5))
