class Solution:
    def kWeakestRows(self,a,k):
        return [h[1] for h in sorted([[j.count(1),i] for i,j in enumerate(a)])[:k]]
    
s=Solution()

print(s.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],3))