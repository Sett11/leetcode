def check(a):
    r=[]
    for i in range(len(a)-1):
        r.append(a[i+1]-a[i])
    return r

class Solution:
    def alternatingSubarray(self,a):
        m=-1
        l=len(a)
        for i in range(l):
            for j in range(i+2,l+1):
                t=a[i:j]
                n=len(t)
                if ([1,-1]*n)[:n-1]==check(t):
                    m=max(m,n)
                else:
                    break
        return m

s = Solution()

print(s.alternatingSubarray([2,3,4,3,4]))