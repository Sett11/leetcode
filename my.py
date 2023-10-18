class Solution:
    def numberOfEmployeesWhoMetTarget(self,a,n):
        return len([i for i in a if i>=n])


s = Solution()

print(s.numberOfEmployeesWhoMetTarget([1, 2, 3, 4,5,6,7,7],5))
