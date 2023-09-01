class Solution:
    def missingNumber(self,a):
        m=max(a)
        for i in range(m+1):
            if i not in a:
                return i
        return m+1
    
s=Solution()

print(s.missingNumber([0,2,3]))