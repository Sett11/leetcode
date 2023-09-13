class Solution:
    def sortEvenOdd(self,a):
        b,c,r=[],[],[]
        for i in range(len(a)):
            if i&1:
                c.append(a[i])
                r.append('even')
            else:
                b.append(a[i])
                r.append('odd')
        b,c=sorted(b),sorted(c,reverse=True)
        return [b.pop(0) if i=='odd' else c.pop(0) for i in r]
    
s=Solution()

print(s.sortEvenOdd([4,1,2,3]))
print(s.sortEvenOdd([36,45,32,31,15,41,9,46,36,6,15,16,33,26,27,31,44,34]))