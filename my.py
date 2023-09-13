class Solution:
    def pivotArray(self,a,n):
        b,c,d=[],[],[]
        [b.append(i) if i<n else c.append(i) if i==n else d.append(i) for i in a]
        return b+c+d
    
s=Solution()

print(s.pivotArray([9,12,5,10,14,3,10],10))
print(s.pivotArray([-3,4,3,2],2))