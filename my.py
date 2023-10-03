class Solution:
    def maxAscendingSum(self,a):
        a.append(a[-1]-1)
        m=max(a,default=0)
        for i in range(len(a)-1):
            if a[i]<a[i+1]:
                for j in range(i+1,len(a)-1):
                    if a[j]>=a[j+1]:
                        m=max(m,sum(a[i:j+1]))
                        break
        return m

s=Solution()

print(s.maxAscendingSum([100,10,1]))