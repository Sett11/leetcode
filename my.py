class Solution:
    def lastStoneWeight(self,a):
        while len(a)>1:
            n=max(a)
            a.remove(n)
            m=max(a)
            a.remove(m)
            v=max(n,m)-min(n,m)
            a.append(v)
        return a[0]

s=Solution()

print(s.lastStoneWeight([2,7,4,1,8,1]))