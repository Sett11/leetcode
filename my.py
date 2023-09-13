class Solution:
    def shuffle(self,a,n):
        b,c,r=a[:n],a[n:],[]
        for i in range(n):
            r.extend([b[i],c[i]])
        return r
    
s=Solution()

print(s.shuffle([2,5,1,3,4,7],3))