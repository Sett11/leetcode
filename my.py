from re import sub

class Solution:
    def minDiffInBST(self,a):
        a=sub(r'[^\d]',' ',repr(a)).split(' ')
        m=1e9
        l=len(a)
        for i in range(l):
            if a[i]:
                t=int(a[i])
                for j in range(i+1,l):
                    if a[j]:
                        m=min(m,abs(t-int(a[j])))
        return m
    
s=Solution()

print(s.minDiffInBST([4,2,6,1,3]))