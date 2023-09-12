class Solution:
    def smallerNumbersThanCurrent(self,a):
        b=sorted(a)
        return [b.index(i) for i in a]
    
s=Solution()

print(s.smallerNumbersThanCurrent([8,1,2,2,3]))
print(s.smallerNumbersThanCurrent([6,5,4,8]))