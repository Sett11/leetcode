class Solution:
    def sortArrayByParityII(self,a):
        b,c,r=[],[],[]
        [c.append(a[i]) if a[i]&1 else b.append(a[i]) for i in range(len(a))]
        [r.extend([b[i],c[i]]) for i in range(len(b))]
        return r
    
s=Solution()

print(s.sortArrayByParityII([4,2,5,7]))
print(s.sortArrayByParityII([36,45,32,31,15,41,9,46,36,6,15,16,33,26,27,31,44,34]))