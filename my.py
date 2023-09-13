class Solution:
    def arrayPairSum(self,a):
        a.sort()
        return sum([min(a[i],a[i+1]) for i in range(0,len(a)-1,2)])
    
s=Solution()

print(s.arrayPairSum([6,2,6,5,1,2]))
print(s.arrayPairSum([1,4,3,2]))