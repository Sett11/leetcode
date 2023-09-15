class Solution:
    def pivotIndex(self,a):
        c=0
        for i in range(1,len(a)+1):
            if c==sum(a[i:]):
                return i-1
            c+=a[i-1]
        return -1
        
s=Solution()

print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([-1,-1,-1,-1,-1,-1]))