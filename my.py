class Solution:
    def repeatedNTimes(self,a):
        return next(i for i in a if a.count(i)==len(a)//2)
    
s=Solution()

print(s.repeatedNTimes([2,1,2,5,3,2]))