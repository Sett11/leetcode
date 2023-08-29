class Solution:
    def topKFrequent(self,a,n):
        s=set(a)
        return [j[1] for j in sorted([[a.count(i),i] for i in s],reverse=True)[:n]]

s = Solution()

print(s.topKFrequent([1,1,1,2,2,3],2))
print(s.topKFrequent([-1,-1],2))
print(s.topKFrequent([4,1,-1,2,-1,2,3],2))
