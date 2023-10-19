class Solution:
    def differenceOfSums(self,n,m):
        a=b=0
        for i in range(1,n+1):
            if not i%m:
                b+=i
            else:
                a+=i
        return a-b


s = Solution()

print(s.differenceOfSums(10,3))
