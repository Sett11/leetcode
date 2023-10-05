class Solution:
    def largestGoodInteger(self,s):
        a=[str(i)*3 for i in range(9,-1,-1)]
        try:
            return next(i for i in a if i in s)
        except:
            return ''
    
s=Solution()

print(s.largestGoodInteger('6777133339'))