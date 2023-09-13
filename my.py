class Solution:
    def rearrangeArray(self,a):
        b,c,r=[],[],[]
        [c.append(a[i]) if a[i]<0 else b.append(a[i]) for i in range(len(a))]
        [r.extend([b[i],c[i]]) for i in range(len(b))]
        return r
    
s=Solution()

print(s.rearrangeArray([3,1,-2,-5,2,-4]))
print(s.rearrangeArray([-1,1]))