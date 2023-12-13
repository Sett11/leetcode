from collections import Counter

class Solution:
    def sortColors(self,a):
        c=Counter(a)
        x=[0]*c[0]+[1]*c[1]+[2]*c[2]

        for i in range(len(x)):
            a[i]=x[i]
    
S=Solution()

print(S.sortColors([2,0,2,1,1,0]))