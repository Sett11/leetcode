class Solution:
    def largestNumber(self,a):
        return sorted([str(i) for i in a],reverse=True)

s=Solution()

print(s.largestNumber([3,30,34,5,9]))
print(s.largestNumber([111311,1113]))