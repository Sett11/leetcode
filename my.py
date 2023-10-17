class Solution:
    def findMaxAverage(self, a, k):
        m=c=sum(a[:k])
        for i in range(k,len(a)):
            c+=a[i]-a[i-k]
            m=max(c,m)
        return m/k


s = Solution()

print(s.findMaxAverage([1,12,-5,-6,50,3], 4))
