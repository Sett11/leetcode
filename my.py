class Solution:
    def rotate(self,a,k):
        for i in range(k):
            a.insert(0,a.pop())
        return a
    
s=Solution()

print(s.rotate([1,2,3,4,5,6,7],3))
print(s.rotate([-1,-100,3,99],2))