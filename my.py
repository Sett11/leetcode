class Solution:
    def plusOne(self,a):
        return [int(j) for j in str(int(''.join([str(i) for i in a]))+1)]
    
s=Solution()

print(s.plusOne([4,3,2,1]))