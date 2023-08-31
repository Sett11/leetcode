class Solution:
    def differenceOfSum(self,a):
        return abs(sum(a)-sum([int(i) for i in ''.join([str(j) for j in a])]))
    
s=Solution()

print(s.differenceOfSum([1,15,6,3]))